import streamlit as st

# Sample help text (can be moved to help.py for better organization)
HELP_TEXT = """
This is a sample leaderboard application built with Streamlit. It displays the top entries from a CSV file with search, sorting, and filtering functionalities (placeholder for filtering). Users can submit scores (currently a placeholder functionality).

**Features:**

* Leaderboard table with search and sorting
* User input section (search)
* Help page

**Data:**

The leaderboard data is loaded from a CSV file. You can modify the data in `leaderboard_data.csv` to suit your needs. Ensure the column names match those specified here (Model, F1 Score, Exact Match Score, Task, Description).

**How to Use:**

1. Enter a search term in the search bar to filter by Description.
2. Click on column headers to sort the table.
3. Explore the leaderboard and help page.

**Note:**

Sorting and filtering functionality might be limited depending on the size of your data.
"""

F1_SCORE_DEFINITION = """
***F1 Score*** is a metric that combines precision and recall. It is calculated as the harmonic mean of precision and recall:
- Precision: The proportion of true positives among the predicted positives.
- Recall: The proportion of true positives among the actual positives.

A higher F1 Score indicates a better balance between precision and recall.
"""

EXACT_MATCH_SCORE_DEFINITION = """
***Exact Match Score*** is the percentage of predictions where all words exactly match the ground truth labels. It measures how well the model predicts the exact sequence of words in the reference answer.

A higher Exact Match Score indicates that the model's predictions are more likely to be identical to the correct answer.
"""

DISCLAIMER = """
YOUR DISCLAIMER TEXT HERE
"""


def display_help_page():
    """Displays the help page."""
    st.subheader("About")
    st.markdown(HELP_TEXT)

    st.subheader("Definition")
    st.markdown(F1_SCORE_DEFINITION)  # Display F1 Score definition
    st.markdown(EXACT_MATCH_SCORE_DEFINITION)  # Display Exact Match Score definition

    st.subheader("Disclaimer")
    st.markdown(DISCLAIMER)  # Display Exact Match Score definition
