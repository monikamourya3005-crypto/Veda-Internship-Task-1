# Day 38: Basic Data Distributions - Data Science Task

This repository contains my solution for **Day 38 (Basic Data Distributions)** of my Data Science internship at Veda Technology. The main goal of this notebook is to look at different data shapes using histograms and understand how mean and median behave when data is skewed.

## What I Used
- Python (on Google Colab)
- NumPy and Pandas for handling data and calculating stats
- Matplotlib and Seaborn for plotting histograms

## Datasets Used
1. **Iris Dataset:** Checked the spread of sepal and petal measurements across different flowers.
2. **Generated Data:** Created simple random numbers using NumPy to clearly show what normal, right-skewed, and left-skewed graphs look like.

## What I Observed
- **Normal Distribution:** The graph looks like a symmetric bell, and the mean and median are almost equal (like in the Sepal Width column).
- **Right-Skewed Data:** The tail stretches out to the right side because of a few high values, which pulls the mean higher than the median.
- **Left-Skewed Data:** The tail stretches to the left side due to some low values, making the mean smaller than the median.
- **Two Peaks (Bimodal):** Petal length and width showed two separate peaks, which makes sense because different flower species in the dataset have different sizes.

## Files in this Repo
- `Day38_Basic_Data_Distributions.ipynb` - The Google Colab notebook with all the code, charts, and notes.
- `README.md` - Basic overview of the Day 38 task.

## How to Run It
Just open the `.ipynb` file in Google Colab or Jupyter Notebook and run the cells from top to bottom to see the charts and summary tables.