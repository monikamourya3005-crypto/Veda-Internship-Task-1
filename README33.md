# Day 33: Train-Test Split Concept

## Veda Technology – Data Science Internship

### Project Overview
This task focuses on understanding and implementing the train-test split technique using Python and Scikit-learn.

Train-test splitting is an important step in machine learning that divides a dataset into two parts:
- **Training Data:** Used to train the machine learning model.
- **Testing Data:** Used to evaluate the model on unseen data.

### Objectives
- Understand the concept of train-test splitting.
- Load and explore a dataset using Pandas.
- Implement 80:20 and 70:30 train-test splits.
- Compare different splitting ratios.
- Understand the importance of `random_state`.
- Maintain class distribution using stratified splitting.

### Tools & Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab / Jupyter Notebook

### Dataset
**Iris Dataset** from Scikit-learn.

The dataset contains 150 samples with four numerical features and three target classes.

### Tasks Performed
1. Imported the required Python libraries.
2. Loaded and explored the Iris dataset.
3. Performed an 80:20 train-test split.
4. Performed a 70:30 train-test split.
5. Compared 80:20, 75:25, and 70:30 splitting ratios.
6. Used `random_state=42` for reproducibility.
7. Applied stratified splitting to maintain class proportions.
8. Displayed the final observations and conclusion.

### Key Concepts
- `train_test_split()` – Divides data into training and testing sets.
- `test_size` – Defines the proportion of testing data.
- `random_state` – Ensures reproducible splitting.
- `stratify` – Maintains class distribution in both sets.

### Results
Successfully implemented different train-test splitting ratios on the Iris dataset.

| Split Ratio | Training Samples | Testing Samples |
|---|---:|---:|
| 80:20 | 120 | 30 |
| 75:25 | 112 | 38 |
| 70:30 | 105 | 45 |

### Conclusion
Through this task, I learned how to split a dataset into training and testing sets using Scikit-learn. I also understood why test data should remain unseen during model training and how reproducibility can be maintained using `random_state`.

### Internship
**Veda Technology – Data Science Internship**  
**Task:** 33 – Train-Test Split Concept