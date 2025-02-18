"""Streamlit app to display persons from the qualification database."""
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import sys
from datetime import datetime

# Database connection parameters
DB_URI = "postgresql://uem4h7dfn2ghbi:p4a86c3b87453876d8f121bba06c7bcc1a2bc98412ccdc47fd7c20bedaaa99eeb@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d9ia9eei6rkq90"

def get_db_connection():
    """Create database connection."""
    st.write("Attempting database connection...")
    try:
        engine = create_engine(DB_URI)
        with engine.connect() as conn:
            st.write("Database connection successful")
            st.session_state['connection_status'] = "Connected"
        return engine
    except Exception as e:
        st.error(f"Database connection failed: {str(e)}")
        st.session_state['connection_status'] = "Failed"
        raise

def load_persons(engine):
    """Load persons data from database."""
    query = """
    SELECT 
        p.id,
        p.first_name,
        p.last_name,
        p.email,
        p.birth_date,
        p.person_id,
        COUNT(pq.qualification_id) as qualification_count
    FROM ttt.ttz_person p
    LEFT JOIN ttt.ttz_person_qualification pq ON p.id = pq.person_id
    GROUP BY p.id, p.first_name, p.last_name, p.email, p.birth_date, p.person_id
    ORDER BY p.last_name, p.first_name
    """
    try:
        st.write("Loading persons data...")
        df = pd.read_sql(query, engine)
        st.write(f"Loaded {len(df)} persons")
        return df
    except Exception as e:
        st.error(f"Failed to load persons data: {str(e)}")
        raise

def load_person_qualifications(engine, person_id):
    """Load qualifications for a specific person."""
    query = """
    SELECT 
        q.qualification_id,
        q.name as qualification_name,
        q.description,
        q.level,
        q.language_id,
        pq.acquired_date,
        pq.expiry_date,
        pq.status,
        pq.valid_from,
        pq.valid_until,
        pq.competency_id
    FROM ttt.ttz_person_qualification pq
    JOIN ttt.ttz_qualification q ON pq.qualification_id = q.qualification_id
    WHERE pq.person_id = %(person_id)s
    ORDER BY q.name
    """
    try:
        st.write(f"Loading qualifications for person {person_id}...")
        person_id = int(person_id)
        df = pd.read_sql(query, engine, params={'person_id': person_id})
        st.write(f"Loaded {len(df)} qualifications")
        return df
    except Exception as e:
        st.error(f"Failed to load qualifications for person {person_id}: {str(e)}")
        raise

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Persons Overview",
        page_icon="👥",
        layout="wide"
    )

    st.title("👥 Persons Overview")
    st.write("View and filter persons and their qualifications")

    # Initialize session state for connection status
    if 'connection_status' not in st.session_state:
        st.session_state['connection_status'] = "Not Connected"

    # Show connection status
    st.sidebar.write(f"Connection Status: {st.session_state['connection_status']}")

    try:
        # Create database connection
        engine = get_db_connection()
        
        # Load data
        with st.spinner("Loading persons data..."):
            df = load_persons(engine)

        # Sidebar filters
        st.sidebar.header("Filters")
        
        # Name filter
        name_filter = st.sidebar.text_input("Filter by name")
        if name_filter:
            mask = (df['first_name'].str.contains(name_filter, case=False, na=False) | 
                   df['last_name'].str.contains(name_filter, case=False, na=False))
            df = df[mask]

        # Qualification count filter
        min_qual, max_qual = st.sidebar.slider(
            "Number of qualifications",
            min_value=int(df['qualification_count'].min()),
            max_value=int(df['qualification_count'].max()),
            value=(int(df['qualification_count'].min()), int(df['qualification_count'].max()))
        )
        df = df[
            (df['qualification_count'] >= min_qual) & 
            (df['qualification_count'] <= max_qual)
        ]

        # Display stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Persons", len(df))
        with col2:
            st.metric("Average Qualifications", f"{df['qualification_count'].mean():.1f}")
        with col3:
            st.metric("Max Qualifications", int(df['qualification_count'].max()))

        # Main data display
        st.subheader("Persons List")
        
        # Format the dataframe for display
        display_df = df.copy()
        display_df.columns = [col.replace('_', ' ').title() for col in display_df.columns]
        
        # Add selection column
        selected_person = st.selectbox(
            "Select a person to view their qualifications:",
            options=df.index,
            format_func=lambda x: f"{df.loc[x, 'first_name']} {df.loc[x, 'last_name']} (ID: {df.loc[x, 'id']})"
        )

        # Display person details
        if selected_person is not None:
            person = df.loc[selected_person]
            st.subheader(f"Details for {person['first_name']} {person['last_name']}")
            
            # Person info in columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**ID:** {person['id']}")
                st.write(f"**Person ID:** {person['person_id']}")
            with col2:
                st.write(f"**Email:** {person['email'] or 'N/A'}")
                st.write(f"**Birth Date:** {person['birth_date'] or 'N/A'}")
            with col3:
                st.write(f"**Total Qualifications:** {person['qualification_count']}")

            # Load and display qualifications
            qualifications_df = load_person_qualifications(engine, person['id'])
            
            if not qualifications_df.empty:
                st.subheader("Qualifications")
                
                # Format dates and nulls
                for col in ['acquired_date', 'expiry_date']:
                    qualifications_df[col] = pd.to_datetime(qualifications_df[col]).dt.strftime('%d.%m.%Y')
                
                # Format the display
                qual_display = qualifications_df.copy()
                qual_display.columns = [col.replace('_', ' ').title() for col in qual_display.columns]
                
                st.dataframe(
                    qual_display,
                    column_config={
                        "Qualification Id": st.column_config.NumberColumn(format="%d"),
                        "Level": st.column_config.NumberColumn(format="%d"),
                        "Competency Id": st.column_config.NumberColumn(format="%d"),
                        "Valid From": st.column_config.NumberColumn(format="%d"),
                        "Valid Until": st.column_config.NumberColumn(format="%d"),
                    },
                    hide_index=True,
                )
                
                # Download qualifications button
                csv = qualifications_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label=f"Download qualifications for {person['first_name']} {person['last_name']}",
                    data=csv,
                    file_name=f"qualifications_{person['id']}.csv",
                    mime="text/csv",
                )
            else:
                st.info("No qualifications found for this person.")

        # Main persons table
        st.subheader("All Persons")
        st.dataframe(
            display_df,
            column_config={
                "Id": st.column_config.NumberColumn(format="%d"),
                "Person Id": st.column_config.NumberColumn(format="%d"),
                "Qualification Count": st.column_config.NumberColumn(format="%d"),
                "Birth Date": st.column_config.DateColumn(format="DD.MM.YYYY"),
            },
            hide_index=True,
        )

        # Download all persons button
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download all persons data as CSV",
            data=csv,
            file_name="persons_data.csv",
            mime="text/csv",
        )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please check your database connection and try again.")
        st.session_state['connection_status'] = "Error"

if __name__ == "__main__":
    main()
