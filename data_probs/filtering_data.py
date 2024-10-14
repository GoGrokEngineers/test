import pandas as pd
import os

# Function to get the next available ID
def get_next_id(output_file):
    if os.path.exists(output_file):
        # Load the output file to find the highest ID
        output_df = pd.read_csv(output_file)
        if 'id' in output_df.columns and not output_df.empty:
            return output_df['id'].max() + 1  # Get the next sequential ID
    return 1  # Start at 1 if the file doesn't exist or is empty

# Function to add tasks to CSV, either from dataset or custom tasks
def add_task_to_csv(input_file, output_file, task_title, custom_description=None, custom_difficulty=None):
    # Step 1: Load the original CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Step 2: Check if the task exists in the dataset
    filtered_df = df[df['title'] == task_title]
    
    # Step 3: Get the next available sequential ID for the task
    next_id = get_next_id(output_file)
    
    if not filtered_df.empty:
        # If the task exists in the dataset, select the columns we need
        selected_columns = filtered_df[['title', 'description', 'difficulty']]
        selected_columns.insert(0, 'id', next_id)  # Insert the sequential ID
    else:
        # If the task does not exist, create a custom entry
        if custom_description is None or custom_difficulty is None:
            print(f"Task '{task_title}' not found in dataset. Please provide description and difficulty for custom entry.")
            return
        else:
            # Create a DataFrame for the custom task
            selected_columns = pd.DataFrame({
                'id': [next_id],
                'title': [task_title],
                'description': [custom_description],
                'difficulty': [custom_difficulty]
            })
    
    # Step 4: Append the data (either from dataset or custom) to the output CSV file
    selected_columns.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))

    print(f"Task '{task_title}' has been added to {output_file} with ID {next_id}.")

# Example usage
input_file = 'leetcode_dataset.csv'  # Input CSV file path
output_file = 'filtered_output_file.csv'  # Output CSV file path

# Add tasks that exist in the dataset

add_task_to_csv(input_file, output_file, 'Binary Tree Maximum Path Sum')  # Task exists

# Add a custom task that is not in the dataset
