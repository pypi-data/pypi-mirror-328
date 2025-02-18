import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import glob
import json
import subprocess
from pathlib import Path
import time

def verify_locators(app_file):
    """Verify that all data-testid locators exist in the app"""
    if not os.path.exists(app_file):
        return [], "App file not found"
    
    with open(app_file, 'r') as f:
        content = f.read()
    
    # Extract all data-testid locators from test files
    test_locators = set()
    for test_file in glob.glob("tests/robot/gui/*.robot"):
        with open(test_file, 'r') as f:
            test_content = f.read()
            import re
            locators = re.findall(r'\[data-testid="([^"]+)"\]', test_content)
            test_locators.update(locators)
    
    # Check which locators exist in app
    missing_locators = []
    for locator in test_locators:
        if f'data-testid="{locator}"' not in content:
            missing_locators.append(locator)
    
    return missing_locators, "OK" if not missing_locators else f"Missing {len(missing_locators)} locators"

def suggest_locator_fix(locator, content):
    """Suggest fixes for broken locators"""
    import re
    from difflib import get_close_matches
    
    # Extract all data-testid attributes from content
    existing_locators = re.findall(r'data-testid="([^"]+)"', content)
    
    # Find similar locators
    similar = get_close_matches(locator, existing_locators, n=3, cutoff=0.6)
    
    # Generate alternative locator strategies
    alternatives = []
    
    # Try semantic HTML elements
    if re.search(r'button|btn', locator, re.I):
        alternatives.append(('button', 'button[contains(text(), "{}")]'.format(locator.replace('-', ' '))))
    elif re.search(r'input|field', locator, re.I):
        alternatives.append(('input', 'input[contains(@placeholder, "{}")]'.format(locator.replace('-', ' '))))
    
    # Try aria labels
    alternatives.append(('aria-label', '[aria-label="{}"]'.format(locator.replace('-', ' ').title())))
    
    return {
        'similar_locators': similar,
        'alternative_strategies': alternatives
    }

def apply_locator_fix(app_file, old_locator, new_locator):
    """Apply a locator fix to the app file"""
    try:
        with open(app_file, 'r') as f:
            content = f.read()
        
        # Replace the locator
        new_content = content.replace(
            f'data-testid="{old_locator}"',
            f'data-testid="{new_locator}"'
        )
        
        with open(app_file, 'w') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        st.error(f"Error applying fix: {str(e)}")
        return False

def update_test_locators(test_file, old_locator, new_locator):
    """Update locators in test files"""
    try:
        with open(test_file, 'r') as f:
            content = f.read()
        
        # Replace the locator in test file
        new_content = content.replace(
            f'[data-testid="{old_locator}"]',
            f'[data-testid="{new_locator}"]'
        )
        
        with open(test_file, 'w') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        st.error(f"Error updating test file: {str(e)}")
        return False

def run_tests(test_path, options=None):
    """Run Robot Framework tests"""
    if options is None:
        options = []
    
    cmd = ["robot", "--outputdir", "tests/robot/results"]
    cmd.extend(options)
    cmd.append(test_path)
    
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Stream output in real-time
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                st.code(output.strip())
        
        return_code = process.poll()
        return return_code == 0
    except Exception as e:
        st.error(f"Error running tests: {str(e)}")
        return False

def load_robot_results(results_dir):
    """Load Robot Framework results from output.xml"""
    results = []
    for xml_file in glob.glob(os.path.join(results_dir, "**/output.xml"), recursive=True):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Get suite information
            for suite in root.findall(".//suite"):
                suite_name = suite.get('name')
                
                # Get test case information
                for test in suite.findall(".//test"):
                    test_name = test.get('name')
                    status = test.find('status')
                    
                    result = {
                        'suite': suite_name,
                        'test': test_name,
                        'status': status.get('status'),
                        'starttime': status.get('starttime'),
                        'endtime': status.get('endtime'),
                        'elapsed': float(status.get('elapsed', 0)),
                        'tags': [tag.text for tag in test.findall('tags/tag')]
                    }
                    results.append(result)
        except Exception as e:
            st.error(f"Error loading results from {xml_file}: {str(e)}")
    
    return pd.DataFrame(results) if results else pd.DataFrame()

def calculate_metrics(df):
    """Calculate test metrics from results DataFrame"""
    if df.empty:
        return {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'pass_rate': 0,
            'avg_duration': 0,
            'total_duration': 0
        }
    
    total_tests = len(df)
    passed_tests = len(df[df['status'] == 'PASS'])
    failed_tests = len(df[df['status'] == 'FAIL'])
    
    metrics = {
        'total_tests': total_tests,
        'passed_tests': passed_tests,
        'failed_tests': failed_tests,
        'pass_rate': (passed_tests / total_tests * 100) if total_tests > 0 else 0,
        'avg_duration': df['elapsed'].mean() if not df.empty else 0,
        'total_duration': df['elapsed'].sum() if not df.empty else 0
    }
    
    return metrics

def plot_test_results(df):
    """Create visualizations for test results"""
    if df.empty:
        st.warning("No test results to display")
        return
    
    # Status distribution
    fig_status = px.pie(
        df, 
        names='status', 
        title='Test Status Distribution',
        color='status',
        color_discrete_map={'PASS': '#00CC96', 'FAIL': '#EF553B'}
    )
    st.plotly_chart(fig_status)
    
    # Test duration by suite
    fig_duration = px.box(
        df, 
        x='suite', 
        y='elapsed',
        title='Test Duration by Suite'
    )
    st.plotly_chart(fig_duration)
    
    # Test status by suite
    status_by_suite = pd.crosstab(df['suite'], df['status'])
    fig_suite = px.bar(
        status_by_suite, 
        title='Test Status by Suite',
        barmode='group'
    )
    st.plotly_chart(fig_suite)

def show_test_details(df):
    """Display detailed test information"""
    st.subheader("Test Details")
    
    if df.empty:
        st.warning("No test results to display")
        return
    
    # Filters
    suites = ['All'] + sorted(df['suite'].unique().tolist())
    selected_suite = st.selectbox('Select Suite', suites)
    
    statuses = ['All'] + sorted(df['status'].unique().tolist())
    selected_status = st.selectbox('Select Status', statuses)
    
    # Filter data
    filtered_df = df.copy()
    if selected_suite != 'All':
        filtered_df = filtered_df[filtered_df['suite'] == selected_suite]
    if selected_status != 'All':
        filtered_df = filtered_df[filtered_df['status'] == selected_status]
    
    # Display results
    st.dataframe(
        filtered_df[['suite', 'test', 'status', 'elapsed', 'tags']],
        use_container_width=True
    )

def render_documentation():
    """Render documentation section"""
    st.header("Documentation")
    
    # Documentation tabs
    doc_tab = st.tabs(["Test Guide", "Self-Healing", "Examples", "API"])
    
    with doc_tab[0]:
        st.markdown("""
        # Robot Framework Test Guide
        
        ## Overview
        ADPA uses Robot Framework for automated testing, providing comprehensive test coverage:
        - GUI Testing
        - API Testing
        - Integration Testing
        
        ## Quick Start
        ```bash
        # Run all tests
        robot --outputdir tests/robot/results tests/robot/gui/
        
        # Run specific test suite
        robot --outputdir tests/robot/results tests/robot/gui/dashboard_tests.robot
        ```
        
        ## Test Structure
        ```
        tests/robot/
        ├── gui/                    # GUI test suites
        │   ├── dashboard_tests.robot
        │   ├── project_tests.robot
        │   └── research_tests.robot
        ├── resources/              # Shared resources
        │   ├── common.resource
        │   └── gui_locators.resource
        └── results/               # Test results
        ```
        """)
        
    with doc_tab[1]:
        st.markdown("""
        # Self-Healing Test System
        
        ## Features
        1. **Locator Analysis**
           - Identifies broken locators
           - Suggests fixes based on similarity
           - Maintains test stability
        
        2. **Fix Strategies**
           ```python
           # Original broken locator
           [data-testid="submit-buttton"]  # Typo
           
           # Auto-fixed locator
           [data-testid="submit-button"]   # Fixed
           ```
        
        3. **Usage**
           - Use "Verify Locators" to check
           - Click "Self Heal" for automatic fixes
           - Review and approve changes
        
        ## Best Practices
        1. Always review automatic fixes
        2. Test fixed locators
        3. Update documentation
        4. Commit changes
        """)
        
    with doc_tab[2]:
        st.markdown("""
        # Test Examples
        
        ## GUI Test
        ```robotframework
        *** Test Cases ***
        Dashboard Should Display Project Overview
            [Documentation]    Verify dashboard shows correct project information
            [Tags]    gui    dashboard    smoke
            
            Open Browser    ${URL}    ${BROWSER}
            Wait Until Element Is Visible    [data-testid="dashboard-title"]
            Element Text Should Be    [data-testid="dashboard-title"]    Project Overview
        ```
        
        ## Resource File
        ```robotframework
        *** Settings ***
        Resource    ../resources/common.resource
        
        *** Variables ***
        ${URL}    http://localhost:8506
        ${BROWSER}    chrome
        
        *** Keywords ***
        Setup Test Environment
            Open Browser    ${URL}    ${BROWSER}
            Maximize Browser Window
        ```
        """)
        
    with doc_tab[3]:
        st.markdown("""
        # API Reference
        
        ## Test Dashboard
        
        ### Functions
        
        #### `verify_locators(file_path: str) -> Tuple[List[str], str]`
        Verifies all locators in test files against the application.
        
        #### `suggest_locator_fix(locator: str, content: str) -> Dict`
        Suggests fixes for broken locators using various strategies.
        
        #### `apply_locator_fix(app_file: str, old_locator: str, new_locator: str) -> bool`
        Applies a locator fix to the application file.
        
        ### Configuration
        
        ```python
        config = {
            'browser': 'chrome',
            'headless': True,
            'screenshot_dir': 'results/screenshots',
            'report_dir': 'results/reports'
        }
        """
        )

def main():
    st.set_page_config(
        page_title="ADPA Test Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("ADPA Test Dashboard")
    
    # Main tabs
    main_tab = st.tabs(["Test Runner", "Documentation", "Results"])
    
    with main_tab[0]:
        # Test controls in sidebar
        st.sidebar.title("Test Controls")
        
        # Verify locators
        st.sidebar.subheader("Locator Verification")
        
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("Verify Locators"):
                missing_locators, status = verify_locators("app.py")
                if missing_locators:
                    st.session_state.missing_locators = missing_locators
                    st.error(f"Missing locators: {', '.join(missing_locators)}")
                else:
                    st.success("All locators found")
        
        with col2:
            if st.button("Self Heal", help="Attempt to automatically fix broken locators"):
                if 'missing_locators' in st.session_state and st.session_state.missing_locators:
                    with st.spinner("Analyzing and fixing locators..."):
                        fixed_count = 0
                        for locator in st.session_state.missing_locators:
                            with open("app.py", 'r') as f:
                                content = f.read()
                            
                            fixes = suggest_locator_fix(locator, content)
                            
                            if fixes['similar_locators']:
                                new_locator = fixes['similar_locators'][0]
                                if apply_locator_fix("app.py", locator, new_locator):
                                    for test_file in glob.glob("tests/robot/gui/*.robot"):
                                        update_test_locators(test_file, locator, new_locator)
                                    fixed_count += 1
                                    st.info(f"Fixed locator: {locator} → {new_locator}")
                            elif fixes['alternative_strategies']:
                                strategy_name, new_locator = fixes['alternative_strategies'][0]
                                st.warning(
                                    f"Could not find similar locator for '{locator}'. "
                                    f"Suggested alternative: {strategy_name} - {new_locator}"
                                )
                        
                        if fixed_count > 0:
                            st.success(f"Fixed {fixed_count} locators")
                            missing_locators, status = verify_locators("app.py")
                            st.session_state.missing_locators = missing_locators
                        else:
                            st.warning("No locators could be automatically fixed")
                else:
                    st.info("No broken locators to fix")
        
        # Test execution section
        st.subheader("Test Execution")
        test_path = st.text_input("Test Path", value="tests/robot/gui/")
        
        col1, col2 = st.columns(2)
        with col1:
            browser = st.selectbox("Browser", ["chrome", "firefox", "edge"])
        with col2:
            headless = st.checkbox("Headless Mode", value=True)
        
        if st.button("Run Tests"):
            options = {
                "browser": browser,
                "headless": headless
            }
            run_tests(test_path, options)
    
    with main_tab[1]:
        render_documentation()
    
    with main_tab[2]:
        st.header("Test Results")
        if os.path.exists("tests/robot/results/output.xml"):
            df = load_robot_results("tests/robot/results")
            metrics = calculate_metrics(df)
            plot_test_results(df)
            show_test_details(df)
        else:
            st.info("No test results available. Run tests to see results here.")

if __name__ == "__main__":
    main()
