# Exam Results

Application for managing exam results, which automates the process of grading and group statistical analysis.

## Features

- **Results Registration**
  Adding scores (0-100) with automatic formatting for student data and subjects.
- **Dynamic Grading**
  The application automatically assigns grade descriptors based on exam points using a threshold system.
- **Pass Verification**
  The system checks if a result meets the passing threshold and assigns the appropriate status.
- **Group Statistics**
  Calculates the average score for the group and displays extreme results (min/max).
- **Data Validation**
  Protects against entering points outside the 0-100 range and verifies the date format.
- **JSON Base**
  Full support for text files - automatic loading at startup and saving when closing the program.

## Technical Details

- **Constants Management**: Uses tuples to make program logic configuration easier.
- **Data Processing**: Efficiently extracts data for statistical calculations using loops and Python's built-in functions.

## How to use

1. Make sure you have Python installed.
2. Run the script using Python:

```bash
python main.py
```
