#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:09:10 2024

@author: emangortey
"""

import streamlit as st
import pandas as pd

file = "/Users/emangortey/Desktop/leaderboard.csv"


def leaderboard_page():
    #st.title('Aviation Language Understanding Evaluation (ALUE)')
    st.markdown("<h1 style='text-align: center; font-size: 35px;'>Aviation Language Understanding Evaluation Benchmark</h1>", unsafe_allow_html=True)
    st.write('The Leaderboard aims to enable the evaluation, benchmarking, and assessment of large language models with aviation datasets and use cases.')
    
    st.empty()  # Add a space
    st.empty()  # Add a space
    
    # Load data from CSV file
    df = pd.read_csv(file)
    
    
    # Create a list of tasks
    tasks = df['Task'].unique().tolist()
    tasks.insert(0, 'All')
    # Create a dropdown select box for tasks
    task = st.selectbox('Select a task:', tasks)
    
    # Filter the DataFrame based on the selected task
    if task != 'All':
        df_task = df[df['Task'] == task]
        
        ## Extract the description of the task
        description = df_task['Description'].iloc[0]
        
        # Drop the task column
        df_task = df_task.drop(columns = ['Task','Description'])
        
    else:
        # Calculate the average score for each entity across all tasks
        df_task = df.groupby('Model', as_index=False)['F1 Score'].mean()
        description = "This table presents the average F1 score for each model across all tasks"
        
        # Drop the task column
        #df_task = df_task.drop(columns = ['Task'])
        
    
 
    df_task = df_task.fillna('')
   
    # Set the width of the columns and center the headers    
    df_styled = df_task.sort_values(by='F1 Score', ascending=True).style.set_table_styles([
        {'selector': 'th', 'props': [('width', '800px'), ('text-align', 'center')]},
        {'selector': 'td', 'props': [('width', '800px')]}
    ])
    
   
    
    # Convert the DataFrame to HTML and remove the index
    table_html = df_styled.hide_index().render()
    
    # Display text
    st.write(description)
   
    
    st.empty()  # Add a space
    st.empty()  # Add a space
    
    # Display the table
    st.write(table_html, unsafe_allow_html=True)
    st.empty()  # Add a space
    st.empty()  # Add a space
    
def form_page():
    # Form
    st.subheader('Evaluate your model')
    
    name = st.text_input('Name')
    email = st.text_input('Email')
    description = st.text_area('Description')
    submit_button = st.button('Submit')
    if submit_button:
        st.write('Name:', name)
        st.write('Email:', email)
        st.write('Description:', description)
        
def benchmarks_page():
    st.title('Benchmarks')
    st.text('Here you can describe the various tasks.')
    st.empty()  # Add a space

def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Leaderboard', 'Benchmarks',' Evaluate Your Model'])
    if page == 'Leaderboard':
        leaderboard_page()
    elif page == 'Evaluate Your Model':
        form_page()
    elif page == 'Benchmarks':
        benchmarks_page()

if __name__ == "__main__":
    main()





