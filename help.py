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


def display_help_page():
    """Displays the help page."""
    st.subheader("Help")
    st.markdown(HELP_TEXT)
