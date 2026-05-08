# Weather Log

A meteorological diary application for tracking daily weather observations and performing basic climate data analysis

## Features

- **Daily Logging**
  Record temperature (supports decimals and negative values), humidity (0-100%), and general weather conditions
- **Data Validation**
  - Temperature: Verified as a numeric float
  - Humidity: Enforced integer range from 0 to 100%
  - Conditions: Enforced choice from a predefined list (sunny, cloudy, etc.)
- **Advanced Statistics**
  - Average temperature calculation (formatted to 2 decimal places)
  - Extreme values identification (Hottest and Coldest days)
- **Weather Dominant**
  Algorithmic calculation of the most frequent weather condition using dictionary-based frequency analysis
- **Data Persistence**
  Automatic saving and loading of the weather database via JSON files

## Technical Details

- **Data Structures**
  Utilizes a list of dictionaries to store logs and a constant tuple for weather conditions
- **Algorithms**
  Implements a manual frequency counter (Mode) using dictionary key-value pair mapping
- **Robustness**
  Uses `try-except` blocks for numeric input validation to prevent program crashes

## How to use

1. Make sure Python is installed.
2. Run the script:

```bash
python main.py
```
