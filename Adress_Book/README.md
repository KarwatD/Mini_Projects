# Address Book

Simple and intuitive application for managing a contact database. It allows you to catalog people, assign them to groups, and quickly find data using a built-in search tool.

## Features

- **Contact Records**
  Adding entries including name and surname, phone number, and email with group assignment.
- **Advanced Search**
  Search contacts using fragments of names or surnames. The search is **case-insensitive**.
- **Intelligent Filtering**
  Display all saved contacts or filter them by a specific group (e.g., family, work).
- **Data Validation**
  1. Email verification (must include "@").
  2. Phone number format control (length validation and "-" support).
  3. Enforced group selection from a predefined list.
- **Data Persistence**
  Full support for JSON files – automatic loading at startup and saving when quitting the program.

## Technical Details

- **DRY Principle**
  A universal display function with an optional argument (`grupa=None`) is used to eliminate code repetition during filtering and searching.
- **Operator `in`**
  Used for efficient string matching and searching within the database.

## How to use

1. Make sure you have Python installed.
2. Run the script using Python:

```bash
python main.py
```
