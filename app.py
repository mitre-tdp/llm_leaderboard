import pandas as pd
import streamlit as st
from help import display_help_page  # Import the help function

# Constants (feel free to customize)
LEADERBOARD_FILE = "./data/leaderboard_data.csv"
MAX_ENTRIES = 10

# F1 Score and Exact Match Score definitions (modify as needed)
F1_SCORE_DEFINITION = """
F1 Score is a metric that combines precision and recall. It is calculated as the harmonic mean of precision and recall:
- Precision: The proportion of true positives among the predicted positives.
- Recall: The proportion of true positives among the actual positives.

A higher F1 Score indicates a better balance between precision and recall.
"""

EXACT_MATCH_SCORE_DEFINITION = """
Exact Match Score is the percentage of predictions where all words exactly match the ground truth labels. It measures how well the model predicts the exact sequence of words in the reference answer.

A higher Exact Match Score indicates that the model's predictions are more likely to be identical to the correct answer.
"""


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


def display_leaderboard(data):
    """Displays the filtered and sorted leaderboard data in a table with search term highlighting."""
    if data is not None:
        st.subheader(f" MITRE LLM Leaderboard ")  # Add emoji for title
        st.markdown(F1_SCORE_DEFINITION)  # Display F1 Score definition
        st.markdown(
            EXACT_MATCH_SCORE_DEFINITION
        )  # Display Exact Match Score definition

        data
        search_term = st.text_input("Search (by all columns)")

        if search_term:
            search_query = (
                rf"<b>{search_term}</b>"  # Wrap search term in bold for highlighting
            )
            filtered_data = data[
                data.apply(
                    lambda x: x.astype(str).str.contains(search_term, case=False)
                )
            ]
            filtered_data.style.applymap(
                lambda s: s.replace(search_query, search_query, regex=True)
            )  # Apply highlighting using style.applymap
        else:
            filtered_data = data

        st.table(
            filtered_data.iloc[:, 1:].sort_values(
                by=st.session_state.get("sort_column", "Description")
            )
        )

    else:
        st.info("Leaderboard data not available.")


def user_input_section():
    """Placeholder for additional user input (filtering - future implementation)"""
    # st.subheader("Filter by Additional Criteria (placeholder)")  # Add filter options here


# No content needed for this section as search is implemented elsewhere


def main():
    """Main function to run the leaderboard application."""
    st.set_page_config(
        page_title="Leaderboard", layout="wide"
    )  # Set wide screen layout

    # Create sidebar and add options
    with st.sidebar:
        selected_page = st.radio("Navigation", ["Leaderboard", "Help"])

    leaderboard_data = load_leaderboard_data()

    if selected_page == "Leaderboard":
        user_input_section()  # Placeholder section (search is in display_leaderboard)
        display_leaderboard(leaderboard_data)
    else:
        display_help_page()


if __name__ == "__main__":
    main()
