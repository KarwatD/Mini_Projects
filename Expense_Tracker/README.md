# Expense Tracker

A console-based personal finance manager designed to track daily expenses and analyze spending habits by category.

## Features

- **Expense Logging**
  Record date, description, amount, and category
- **Category Management**
  Ensures data consistency using predefined set of categories
- **Financial Analytics**
  Summarizes total spending and provides a detailed breakdown per category
- **Persistence**
  Saves and loads data from `wydatki.json`

## Technical Details

- **Validation**
  Strict date format (YYYY-MM-DD) and positive numeric verification for amounts
- **Data Integrity**
  Category validation against a tuple constant to prevent incorrect entries
- **Efficiency**
  Uses in-memory processing for statistics before saving to JSON database

## How to use

1. Make sure you have Python installed
2. Run the script:

```bash
python main.py
```
