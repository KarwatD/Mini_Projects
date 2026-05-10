# Personal Sports Records

Sports records tracking application designed to streamline the work of teachers and trainers. It enables quick verification of students' personal bests (lowest times or highest reps), making the grading and progress monitoring process significantly faster and more accurate

## Features

- **Automated Personal Best Logic**
  Intelligent system that distinguishes between time-based disciplines and rep-based disciplines
- **Real-time Record Management**
  Automatically identifies new records upon entry and updates previous ones to maintain a single "current best" for each discipline
- **Discipline Filtering**
  View all sports history or filter results for a specific student/athlete discipline
- **Quick Records Overview**
  Dedicated view to display only current top performances across all categories
- **Dynamic Units**
  Automatically assigns units(mins,reps) based on the selected activity to ensure data consistency

## Technical Details

- **Robust Input Validation**
  Custom-built `num()` function handles data type enforcement and range checks, preventing application crashes from invalid user input
- **JSON Data Persistence**
  All records are stored in a structured JSON database, allowing for easy data portability and persistent storage between sessions
- **Scalable Architecture**
  Built with a modular structure (separate functions for logic and data I/O), making it easy to extend with new sports or more complex grading rules
- **Clean Data Formatting**
  Implements organized console output with clear flags for personal records (!!! REKORD !!!) for better user experience

## How to use

1. Make sure you have Python installed
2. Run script using Python:

```bash
python main.py
```
