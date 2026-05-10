# Sleep Tracker (Python)

A professional console application designed to track and analyze sleep patterns. The program focuses on data precision, handling 24-hour cycle transitions, and providing meaningful health statistics

## Key Features

- **Precise Sleep Logging**
  Register date, bedtime, and wake-up time (HH:MM format) with a subjective quality rating
- **Smart Time Calculator**
  Custom algorithm that calculates sleep duration with minute precision, correctly handling overnight sleep (e.g., from 22:30 to 07:15) using a 1440-minute daily cycle
- **Dynamic Quality Mapping**
  Uses nested tuples to map numeric ratings (1-5) to descriptive labels (e.g., "Very Poor" to "Very Good") through iterative searching
- **Health Analytics**
  Calculates average sleep duration and average sleep quality
- **Deficit Analysis**
  Automatically tracks the number of nights with less than 7 hours of sleep
- **Data Persistence**
  Full JSON integration for saving and loading the sleep history

## Technical Highlights

- **Minute-Level Accuracy**
  Input strings are parsed using .split(':') and converted to total minutes to ensure mathematical correctness before being stored as rounded floats
- **Robust Input Validation**
  Utilizes a custom num() function to handle menu selections and range checks, preventing crashes on invalid user input
- **Data Consistency**
  Enforces strict range limits for sleep quality (1-5) and time formats, ensuring the integrity of the JSON database

## How to use

1. Ensure Python is installed
2. Run the script:

```bash
python main.py
```
