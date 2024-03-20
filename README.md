# MITRE LLM Leaderboard

This Streamlit application displays a leaderboard of Large Language Models (LLMs) based on their performance on a specific task.

## Features

- Filter by model (optional).
- View average F1 score and Exact Match score for each task.
- Grouped data by task.
- Displays all data columns (including model name, F1 score, Exact Match score, etc.).
- Clear and concise interface.

## Getting Started

**Prerequisites:**

- Python 3.x
- Streamlit library (`pip install streamlit`)
- Pandas library (`pip install pandas`)

**Steps:**

1. **Clone the repository:**

   ```bash
   git clone https://gitlab.mitre.org/kkwon/llm_leaderboard.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd leaderboard-repo
   ```

3. **Run the application:**

   ```bash
   streamlit run app.py
   ```

**Using the Leaderboard:**
Open <http://localhost:8501/> in your web browser.
(Optional) Use the filter dropdown to select a specific model.
The leaderboard displays the average F1 score and Exact Match score for each task, along with all other data columns.
