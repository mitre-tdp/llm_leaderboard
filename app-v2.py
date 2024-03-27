import streamlit as st
import pandas as pd
from help import display_help_page  # Import the help function

# Define leaderboard file path
LEADERBOARD_FILE = "./data/Benchmark_Results.csv"


# Function to read CSV and return desired columns
def get_data():
    df = pd.read_csv(LEADERBOARD_FILE)
    return df


# Set wide mode, title, and icon
st.set_page_config(
    page_title="MITRE LLM Leaderboard",
    layout="wide",
    page_icon="",
)

# Title and subtitle
st.header(
    f" 🏆 Aviation Language Understanding Evaluation Benchmark "
)  # Add emoji for title
st.write(
    f"The Leaderboard aims to enable the evaluation, benchmarking, and assessment of large language models with aviation datasets and use cases."
)  # Add emoji for title

def display_leaderboard():
    # Read data
    df = get_data()

    # Unique tasks with "All" option
    task_options = ["All"] + df["Task"].unique().tolist()  # Prepend "All"

    # Entire display area as a container
    container = st.container()

    # Columns inside the container for layout
    col1, col2 = container.columns(2)

    # User selection for task (in left column)
    with col1:
        selected_task = st.selectbox("Select Task", task_options)

    # User selection for model (in right column, appears only if a task is chosen)
    selected_model = None  # Initialize selected_model outside the if block
    if selected_task != "All":
        with col2:
            # Get unique models for the chosen task
            unique_models = ["All"] + df[df["Task"] == selected_task][
                "Model"
            ].unique().tolist()  # Prepend "All"
            selected_model = st.selectbox("Select Model", unique_models)

    # Filter data by selected task and model (combined logic)
    if selected_task == "All":
        df_filtered = df.copy()
    elif selected_model != "All":  # Filter by both task and model if model is not "All"
        df_filtered = df[(df["Task"] == selected_task) & (df["Model"] == selected_model)]
    else:  # Filter by task only if model is "All"
        df_filtered = df[df["Task"] == selected_task]

    # Sort data by Task, Model, and F1 Score (descending) within each task
    df_filtered = df_filtered.sort_values(
        by=["Task", "Model", "F1 Score"], ascending=[True, True, False]
    )

    # Description columns inside the container (shown even if "All" task)
    col_desc1, col_desc2 = container.columns(2)

    # Display task description (left column)
    with col_desc1:
        st.markdown(
            f"""**Task Description:**

    {df_filtered['Task Description'].iloc[0]}  # Access description from first row
    """
        )

    # Conditionally display model description (right column)
    if selected_model:  # Check if selected_model is not None
        with col_desc2:
            # Get model description (assuming "Model Description" column exists)
            model_description = df_filtered[df_filtered["Task"] == selected_task][
                "Model Description"
            ].iloc[0]

            # Handle empty model description
            if pd.isna(model_description):
                model_description = "Not available"

            st.markdown(
                f"""**Model Description:**

    {model_description}
    """
            )

    # Display initial table (with title "Results")
    for _ in range(10):
        st.write("")
    st.subheader("Results")  # Add a subheader for the table
    st.dataframe(
        df_filtered[["Task", "Model", "F1 Score", "Exact Match"]],
        hide_index=True,
        width=1200,
    )


def main():
    """Main function to run the leaderboard application."""


    # Display the selected page
    tab_home, tab_help = st.tabs(["Home", "Help"])
    with tab_home:
        display_leaderboard()

    with tab_help:
        display_help_page()


if __name__ == "__main__":
    main()
