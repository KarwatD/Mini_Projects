# Studying Time Tracker

Console application used to tracking time spent on studying subjects. Program allows save session, analyse effeciency and balance between different fields of knowledge

## Features

- **Session Logging**
  Data registration, subject, time spent and optional notes
- **Advanced statistics**
  Automatically calculate all study time and detailed compete for every subject
- **Leader analysis**
  System automatically finds subject with higest and lowest time spent value
- **Data Filtering**
  Possibility to display full sessions history or filter entries by subject
- **Data Robustness**
  Full support for JSON files - data is saved on quitting and loaded automaticaly

  ## Technical Details
  - **Robust Input Validation**
    Used my own validating funciton `num()`, which eliminates risk of program errors caused wrong input data

- **Effiecency Optimalization**
  Statistics funciton was created using dictionary keys, what assures quick working even with huge amount of sessions
- **Data Cohesion**
  System enforces choice from predefined list, what guarantees order in data base and correctness of generated raports

## How to use:

1. Make sure you have Python installed
2. Run script using Python:

```bash
python main.py
```
