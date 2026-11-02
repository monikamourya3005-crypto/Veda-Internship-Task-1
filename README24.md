# Day 24: Merge and Join DataFrames

## 📌 Project Overview
This task focuses on combining related DataFrames using the Pandas `merge()` function. Different types of joins are explored to understand how multiple datasets can be combined based on common keys.

## 🎯 Objectives
- Understand the concept of merging DataFrames.
- Perform Inner, Left, Right, and Outer joins.
- Identify common keys between datasets.
- Compare the results of different join types.
- Detect unmatched records and create a final combined dataset.

## 🛠️ Tools and Technologies
- Python
- Pandas
- Google Colab / Jupyter Notebook

## 📚 Concepts Covered
- DataFrame Merging
- `pd.merge()` function
- Inner Join
- Left Join
- Right Join
- Outer Join
- Handling unmatched records
- Data Analysis using Pandas

## 📝 Tasks Performed
1. Created sample customer and order DataFrames.
2. Identified the common key between datasets.
3. Performed Inner, Left, Right, and Outer joins.
4. Compared the results of different join methods.
5. Identified unmatched customer and order records.
6. Analyzed the combined dataset.

## 📊 Key Learning Outcomes
- Learned how to combine multiple datasets using Pandas.
- Understood the differences between join types.
- Practiced handling unmatched records.
- Improved data manipulation and analysis skills.

## 💻 Sample Code
```python
# Merge two DataFrames using a common key
merged_df = pd.merge(
    customers,
    orders,
    on='Customer_ID',
    how='inner'
)

display(merged_df)
```

## 📁 Deliverables
- Jupyter Notebook containing the implementation.
- At least four join examples.
- Comparison of join results.
- Final combined dataset.

## ✅ Conclusion
Successfully completed Day 24 of the Veda Technology Data Science Internship by practicing different DataFrame merging techniques using Python and Pandas.

#VedaTechnology #DataScienceInternship #Python #Pandas #DataAnalysis #LearningJourney