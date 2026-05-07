# Book Catalog

Personal system to managing books collection, it allows to track proggres in reading and analyse your library statistics

## Features
* **Entry Management**
  Adding books with informations about title, author, genre and status
* **Double-Layer Validation**
  Application's blocking entering wrong genre or status - it enforces choice from constans list
* **Error Handling**
  When application gets wrong data it's gonna display information and list available options
* **Reading Analysis**
  Automatically calculate number of books in library, read/planned books and designates favourite genre (most read)
* **Session Management**
  Data is stored in memory during program work and saved to JSON file when program is closed (option 0)

## Technical details
* **Statistics Logic**
  Favourite genre is calculated dynamicaly by counting books with status 'przeczytana'
* **Security**
  Application is resilient against empty data bases and wrong input data types (letters instead numbers)

## How to use
1. Make sure you have installed Python
2. Run script using Python:
```bash
python main.py
```
  