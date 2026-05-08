# Grade Tracker

Simple but functional system to checking school grades. It allows to track studying results, calculate average and analyse progress using statistics

## Features
* **Grades Logging**
  Adding entries including description, grades (1-6) and date of getting this grade
* **Calculating Average**
  Automaticaly calculates arithmetic average of all grades rounded to two decimal places
* **Automatical Word-grade**
  System based on calculated average attribute right grade description
* **Extreme Statistics**
  Quick view on best and worst grade in notebook
* **Data Validation**
  Secure from entering wrong grades (out of scale) and enforce right date format
* **Data Persistence** 
  Full support for JSON files - application load history at the start and save when closing application

## Technical Details
* Using tuples iteration to mapping numerical values on words descriptions
* Using build-in functions `min(), max()` to optimize statistical calculations

## How to use
1. Make sure you have Python installed
2. Run script using Python:
```bash
Python main.py
```