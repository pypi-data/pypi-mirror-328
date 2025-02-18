"""Agent Management Streamlit Page."""
import plotly.graph_objects as go
import streamlit as st
from config.models import AgentStatus, LLMConfig

# Initialize session state
if "agents" not in st.session_state:
    st.session_state.agents = []

if "current_agent" not in st.session_state:
    st.session_state.current_agent = None


def stop_running_agent(agent_id: str) -> None:
    """Stop a running agent.

    Args:
        agent_id: ID of the agent to stop
    """
    try:
        agent = next((a for a in st.session_state.agents if a["name"] == agent_id), None)
        if agent:
            agent["status"] = AgentStatus.STOPPED
            st.success("Agent stopped successfully")
        else:
            st.warning("Agent not found")
    except KeyError as e:
        st.error(f"Invalid agent data structure: {str(e)}")
    except Exception as e:
        st.error(f"Failed to stop agent: {str(e)}")


def count_agents_by_provider(provider: str) -> int:
    """Count agents using a specific provider.

    Args:
        provider: LLM provider name

    Returns:
        Number of agents using the provider
    """
    return len([
        a for a in st.session_state.agents
        if a["llm_config"].primary_provider == provider
    ])


def display_agent_metrics() -> None:
    """Display agent performance metrics."""
    try:
        if not st.session_state.agents:
            st.info("No agents available")
            return

        providers = ["OpenAI", "Anthropic", "Gemini", "Groq"]
        colors = {
            "OpenAI": "#10A37F",
            "Anthropic": "#5436DA",
            "Gemini": "#4285F4",
            "Groq": "#FF6B6B"
        }

        # Create metrics visualization
        fig = go.Figure()

        for i, provider in enumerate(providers, 1):
            fig.add_trace(go.Bar(
                name=provider,
                x=[i],
                y=[count_agents_by_provider(provider)],
                marker={"color": colors[provider]}
            ))

        fig.update_layout(
            title="Agents by LLM Provider",
            xaxis={
                "ticktext": providers,
                "tickvals": list(range(1, len(providers) + 1)),
                "title": "Provider"
            },
            yaxis={"title": "Number of Agents"},
            showlegend=False
        )

        st.plotly_chart(fig)

    except ValueError as e:
        st.error(f"Invalid data format: {str(e)}")
    except Exception as e:
        st.error(f"Failed to display metrics: {str(e)}")


def main() -> None:
    """Main function for the agent management page."""
    try:
        st.set_page_config(
            page_title="Agent Management",
            page_icon="🤖",
            layout="wide",
        )
    except Exception as e:
        st.error(f"Failed to set page config: {str(e)}")
        return

    st.title("🤖 Agent Management")

    # Sidebar
    with st.sidebar:
        st.header("Create New Agent")

        try:
            name = st.text_input("Agent Name")
            description = st.text_area("Description")

            llm_config = LLMConfig(
                primary_provider=st.selectbox(
                    "LLM Provider",
                    ["OpenAI", "Anthropic", "Gemini", "Groq"]
                ),
                model=st.text_input("Model Name", value="gpt-4")
            )

            if st.button("Create Agent"):
                if name and description:
                    new_agent = {
                        "name": name,
                        "description": description,
                        "llm_config": llm_config,
                        "status": AgentStatus.READY
                    }
                    st.session_state.agents.append(new_agent)
                    st.success("Agent created successfully!")
                else:
                    st.warning("Please fill in all required fields")

        except ValueError as e:
            st.error(f"Invalid input: {str(e)}")
        except Exception as e:
            st.error(f"Failed to create agent: {str(e)}")

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Active Agents")

        for agent in st.session_state.agents:
            with st.expander(f"{agent['name']} ({agent['status'].value})"):
                st.write(f"Description: {agent['description']}")
                st.write(f"LLM Provider: {agent['llm_config'].primary_provider}")
                st.write(f"Model: {agent['llm_config'].model}")

                if agent["status"] == AgentStatus.RUNNING:
                    if st.button("Stop", key=f"stop_{agent['name']}"):
                        stop_running_agent(agent["name"])
                elif agent["status"] == AgentStatus.READY:
                    st.button("Start", key=f"start_{agent['name']}")

    with col2:
        st.header("Metrics")
        display_agent_metrics()


if __name__ == "__main__":
    main()
