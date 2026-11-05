# Day 27: Reading and Writing Excel Data

## 📌 Project Overview
This task focuses on reading, processing, and writing Excel files using Python and Pandas. It demonstrates how Excel data can be loaded, inspected, transformed, and exported for further analysis.

## 🎯 Objectives
- Read Excel files using Pandas.
- Inspect the structure and data types of Excel datasets.
- Perform basic data cleaning and transformation.
- Filter and sort Excel data.
- Export processed data into Excel files.

## 🛠️ Tools and Technologies
- Python
- Pandas
- NumPy
- OpenPyXL
- Google Colab / Jupyter Notebook

## 📚 Concepts Covered
- `pd.read_excel()`
- `DataFrame.to_excel()`
- Data Inspection
- Missing Value Handling
- Data Filtering
- Data Transformation
- Data Sorting
- Excel File Export

## 📝 Tasks Performed
1. Created a sample employee dataset.
2. Saved the dataset as an Excel file.
3. Read Excel data using Pandas.
4. Inspected dataset structure and data types.
5. Checked and handled missing values.
6. Filtered employees based on department and salary.
7. Created new columns for annual salary and experience level.
8. Sorted employee records by salary.
9. Exported the processed dataset into Excel.
10. Verified and downloaded the final Excel file.

## 📊 Key Learning Outcomes
- Learned how to work with Excel files using Python.
- Practiced reading and writing Excel datasets.
- Improved data cleaning and transformation skills.
- Understood how to prepare Excel data for analysis.

## 💻 Sample Code
```python
# Read an Excel file
df = pd.read_excel('employees.xlsx')

# Export processed data
df.to_excel('processed_employees.xlsx', index=False)
```

## 📁 Deliverables
- Jupyter Notebook containing the implementation.
- Sample Excel dataset.
- Processed Excel output file.

## ✅ Conclusion
Successfully completed Day 27 of the Veda Technology Data Science Internship by practicing Excel data handling and processing using Python and Pandas.

#VedaTechnology #DataScienceInternship #Python #Pandas #Excel #DataAnalysis #LearningJourney