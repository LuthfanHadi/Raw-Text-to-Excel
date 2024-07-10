# Read Text to Excel Project

## Description

This project is a Python program consisting of several modules for managing documentation restart and clean memory instances on server. Program input is txt file that have contain log of history for restart and clean memory instances. After that the program do parsing the log and save it as xlx. Below is a description of each module:

### Modules

1. **ReadZclean.py**: 
   - This module extends `TaskList` and includes methods to parse specific parts of a task, such as date, time, and instance name from a given cell.
   - Key methods include:
     - `get_date`: Extracts the date.
     - `get_row_split`: Splits a cell by newline characters.
     - `get_time`: Calculates start time, escalation time, response time, and end time.
     - `get_instance`: Extracts instance names.
     - `run`: Executes the overall task of reading a file, extracting data, and creating an Excel file.

2. **TaskList.py**: 
   - This module defines the base class `TaskList`, which handles the general structure of a task list.
   - Key methods include:
     - `get_file_name`: Prompts user for the file name.
     - `read_file`: Reads data from the specified file.
     - `get_row_split`: Splits a cell by newline characters.
     - `input_df`: Appends task data to a DataFrame.
     - `create_excel`: Outputs the DataFrame to an Excel file.

3. **main.py**: 
   - This module appears to be the main entry point for running the program.
   - It imports and utilizes the `TaskList` class to perform tasks.
   - Key methods include:
     - `input_month`: Prompts user for the month/year.
     - `read_file`: Reads data from the specified file.
     - `get_date`: Extracts the date.
     - `get_time`: Calculates start time, escalation time, response time, and end time.
     - `get_user`: Extracts the user.
     - `get_instance`: Extracts instance names.
     - `input_df`: Appends task data to a DataFrame.
     - `create_excel`: Outputs the DataFrame to an Excel file.
     - `get_row_split`: Splits a cell by newline characters.
     - `run`: Executes the overall task of reading a file, extracting data, and creating an Excel file.

4. **readrestartinstance.py**: 
   - This module appears to handle reading and restarting instances, extending the functionalities of `TaskList`.
   - Key methods include:
     - `input_month`: Prompts user for the month/year.
     - `read_file`: Reads data from the specified file.
     - `get_date`: Extracts the date.
     - `get_time`: Calculates start time, escalation time, response time, and end time.
     - `get_user`: Extracts the user.
     - `get_instance`: Extracts instance names.
     - `input_df`: Appends task data to a DataFrame.
     - `create_excel`: Outputs the DataFrame to an Excel file.
     - `get_row_split`: Splits a cell by newline characters.
     - `run`: Executes the overall task of reading a file, extracting data, and creating an Excel file.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/LuthfanHadi/Raw-Text-to-Excel.git

