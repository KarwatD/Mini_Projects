# Run Tracker

A console-based activity log designed to track running performance and calculate statistics.

## Features

- **Data Entry**
  Logs date (YYYY-MM-DD), distance and time
- **Auto-Calculation**
  Calculates pace (min/km) automatically
- **Statistics Module**
  Displays total distance, average pace, and total number of sessions
- **Persistence**
  Saves and loads data from `dziennik_biegania.json`

## Technical Details

- **Validation**
  Strict date format check and positive number verification using `try/except`
- **Constraints**
  Minimum distance enforced via tuple constant
- **Architecture**
  Separation of data processing and user interface

## How to use

1. Make sure you have installed Python
2. Download main.py
3. Run the script using Python:

```bash
python main.py
```
