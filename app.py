import pandas as pd
import streamlit as st
from help import display_help_page  # Import the help function

# Constants (feel free to customize)
LEADERBOARD_FILE = "./data/Benchmark_Results.csv"
MAX_ENTRIES = 10


def load_leaderboard_data():
    """Loads leaderboard data from a CSV file."""
    try:
        df = pd.read_csv(LEADERBOARD_FILE)
        return df
    except FileNotFoundError:
        st.error(f"Error: Leaderboard data file '{LEADERBOARD_FILE}' not found.")
        return None


# def display_leaderboard(data):
#     """Displays the filtered and sorted leaderboard data in a table."""
#     # ... (search filtering logic) ...
#     st.table(filtered_data.sort_values(by=st.session_state.get("sort_column", "Model")))


def format_details(details_text):
    """Formats details text for display in a popup."""
    return f"<p style='font-family:sans-serif; color:black; white-space: pre-wrap;'>{details_text}</p>"


def display_leaderboard(data):
    """Displays the filtered and sorted leaderboard data in a table with search term highlighting."""
    if data is not None:
        st.header(
            f" 🏆 Aviation Language Understanding Evaluation Benchmark "
        )  # Add emoji for title
        st.write(
            f"The Leaderboard aims to enable the evaluation, benchmarking, and assessment of large language models with aviation datasets and use cases."
        )  # Add emoji for title

        # Add model selection dropdown with "All" option
        model_options = ["All"] + data["Task"].unique().tolist()
        selected_model = st.selectbox("Select a task:", model_options)

        if selected_model == "All":
            filtered_data = data.copy()
        else:
            filtered_data = data[data["Task"] == selected_model]

        st.write("Entire dataset")
        filtered_data

        if filtered_data.empty:
            st.info("No data to display")
        # else:
        #     # Proceed with formatting and display
        #     st.table(
        #         filtered_data.style.format("Model").to_html(
        #             escape=False, full_width=True, index=False
        #         )
        #     )

        # st.table(
        #     filtered_data.style.format(
        #         "Model", format_details
        #     ).to_html(escape=False, full_width=True, index=False)
        # )

        # Group-by calculations
        grouped_data = (
            filtered_data.groupby("Task")
            .agg(
                Avg_F1_Score=("F1 Score", "mean"),
                Avg_Exact_Match_Score=("Exact Match", "mean"),
            )
            .reset_index()
            .sort_values(
                by="Avg_F1_Score", ascending=False
            )  # Sort by Avg_F1_Score (optional)
        )

        grouped_data

        # Concatenate group-by results with original data for all columns
        # all_data = pd.concat([filtered_data, grouped_data], ignore_index=True)

        # all_data

    else:
        st.info("Leaderboard data not available.")


def user_input_section():
    """Placeholder for additional user input (filtering - future implementation)"""
    # st.subheader("Filter by Additional Criteria (placeholder)")  # Add filter options here


# No content needed for this section as search is implemented elsewhere

def config():
    st.set_page_config(
        page_title="MITRE LLM Leaderboard",
        layout="wide",
        page_icon="🏆",
    )

def main():
    """Main function to run the leaderboard application."""

    # Set page configuration



    # Create navigation using Streamlit functions
    # selected_page = st.sidebar.selectbox("Navigation", ["Home", "Help"])

    # Load leaderboard data
    leaderboard_data = load_leaderboard_data()

    # Display the selected page
    tab_home, tab_help = st.tabs(["Home", "Help"])
    with tab_home:
        user_input_section()
        display_leaderboard(leaderboard_data)
    
    with tab_help:
        display_help_page()


if __name__ == "__main__":
    config()
    main()
