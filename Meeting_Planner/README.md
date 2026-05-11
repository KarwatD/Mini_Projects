# Meeting Planner

A comprehensive meeting and event management system designed to track social outings, guest lists, and event statuses with high data integrity

## Key Features

- **Event Management** Add events with detailed metadata, including name, date, location, and guest lists
- **Flexible Status Tracking** Manage the lifecycle of an event by updating its status (Planned, Completed, Cancelled)
- **Smart Data Filtering** Integrated view system that allows browsing the entire history or filtering specifically by event status
- **Advanced Date Validation** Custom logic enforcing the ISO 8601 (YYYY-MM-DD) format. The system accepts both dots and dashes, automatically normalizing them and validating calendar ranges
- **Data Persistence** Full synchronization with a JSON database for reliable data storage between sessions

## Technical Details

- **Data Normalization** The system automatically converts various date separators into a unified standard (YYYY-MM-DD) before saving, ensuring a clean and sortable database
- **Efficient Function Architecture**
  The display engine uses optional arguments to handle both general views and filtered queries within a single, optimized block of code
- **Robust Input Validation**
  Prevents logical errors by validating user input against predefined allowed categories (locations and statuses) using a custom validation engine

## How to Use

1. Make sure you have Python installed
2. Run script using Python:

```bash
python main.py
```
