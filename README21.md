# Day 21: Date Parsing and Datetime Basics

## 📌 Project Overview
This task focuses on converting text-based dates into Pandas datetime objects and extracting useful date information such as year, month, day, and weekday using Python and Pandas.

## 🎯 Objective
- Convert string-based dates into datetime format.
- Identify and handle invalid date values.
- Extract year, month, day, and weekday information.
- Perform date-based filtering and analysis.

## 🛠️ Tools and Technologies
- Python
- Pandas
- NumPy
- Google Colab / Jupyter Notebook

## 📚 Concepts Covered
- `pd.to_datetime()` for date conversion
- `errors="coerce"` for handling invalid dates
- `isna()` for identifying missing date values
- `.dt` accessor for extracting date components
- Year, month, day, and weekday extraction
- Date-based filtering
- GroupBy for date-based sales analysis

## 💻 Tasks Implemented

### 1. Dataset Creation and Inspection
- Created a sample sales dataset.
- Inspected DataFrame information and data types.
- Examined the original date column.

### 2. Date Conversion
- Converted string dates into Pandas datetime format.
- Handled invalid date values using `errors="coerce"`.
- Identified and removed invalid date records.

### 3. Datetime Extraction
Created new columns for:
- Year
- Month
- Day
- Weekday
- Weekday Number

### 4. Date-Based Filtering
- Filtered orders from the first quarter.
- Selected orders from July 2025 onwards.
- Practiced date-based conditions.

### 5. Date-Based Analysis
- Calculated total orders and sales.
- Calculated average sales.
- Analyzed monthly sales.
- Compared sales across weekdays.
- Counted orders year-wise.

## 📈 Learning Outcomes
Through this task, I learned how to work with datetime values in Pandas, handle invalid dates, extract meaningful date components, and perform date-based data analysis.

## ✅ Conclusion
Date parsing and datetime extraction are important steps in data preprocessing. They help transform raw date values into useful information for filtering, grouping, and analyzing datasets.

## 📂 Repository Contents
- `Veda_Day21_Date_Parsing_Datetime_Basics.ipynb` — Notebook containing code examples and outputs.
- `README21.md` — Task overview, concepts, and learning outcomes.

**Internship:** Veda Technology  
**Track:** Data Science  
**Task:** Day 21
