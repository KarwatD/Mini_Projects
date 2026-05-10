# TasksList

A simple and efficient task manager to organize daily duties with priorities and status tracking.

## Features

- **Entry Management**
  Add tasks with descriptions and selectable priority levels
- **Status Tracking**
  Interactive system to mark tasks as completed using their list numbers
- **Smart Filtering**
  Advanced display function using default arguments to toggle between the full list and pending tasks only
- **Data Integrity**
  Validation for priorities (via constants) and range checking for task numbers using try/except blocks to prevent errors
- **State Preservation**
  Data is stored in-memory during execution and persisted to a JSON file upon graceful exit (Option 0)

## Technical Details

- **Default Arguments**
  Implementation of optional parameters in functions to handle different view modes
- **List & Dictionary Mapping**
  Utilizes index-based mapping (index = number - 1) for direct data manipulation within the task list

## How to use

1. Make sure you have Python installed
2. Run the script:
   ```bash
   python main.py
   ```
