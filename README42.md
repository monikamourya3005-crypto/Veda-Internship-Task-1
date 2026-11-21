# Day 41 – Customer Segmentation & Service Recommendation System

## Project Overview
This project develops a customer analytics system that groups customers based on their behavior, interests, engagement, service inquiries, spending, and interaction patterns.

K-Means clustering is used to identify customer segments, while a rule-based recommendation system suggests suitable learning programs and technology services.

## Objective
To understand unsupervised learning, customer segmentation, feature engineering, clustering evaluation, PCA, and recommendation logic.

## Problem Statement
Analyze customer behavior and divide customers into meaningful groups to provide more relevant service and learning program recommendations.

## Dataset Description
- **Dataset:** Synthetic Customer Dataset
- **Records:** 500 sample customers
- **Features:** Age, Interest, Engagement Score, Service Inquiries, Monthly Spending, Interactions, and Course Completion Rate.
- **Target:** No predefined target variable; clustering is an unsupervised learning task.

**Note:** The dataset is artificially generated for learning and demonstration. It does not contain actual Veda Technology customer information.

## Tools and Technologies
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- K-Means Clustering
- PCA
- Streamlit
- Google Colab

## Project Workflow

1. Customer dataset generation and loading
2. Data cleaning and preprocessing
3. Customer behavior analysis
4. Data visualization
5. Feature engineering
6. Feature scaling
7. K-Means clustering
8. Cluster evaluation using Silhouette Score
9. PCA-based cluster visualization
10. Customer segment profiling
11. Personalized service recommendation logic
12. Streamlit dashboard creation

## Machine Learning Approach

**Algorithm:** K-Means Clustering

K-Means groups customers into four clusters based on their numerical behavior features.

**PCA:** Principal Component Analysis reduces the feature dimensions to two components for visualization.

**Evaluation:** Silhouette Score is used to evaluate cluster separation.

## Customer Segmentation
Customers are grouped into four behavior-based segments:
- Low Engagement Customers
- Developing Customers
- Active Customers
- Highly Engaged Customers

The segment labels are assigned according to the average engagement score of each cluster.

## Recommendation System
Recommendations are generated using customer interests, engagement scores, course completion rates, and service inquiries.

Example recommendations include:
- Data Science Training Program
- Full Stack Web Development Program
- Artificial Intelligence and ML Program
- Advanced Python Programming Course
- Cloud Computing Fundamentals

These are illustrative recommendations, not an official Veda Technology service catalog.

## Key Findings
The project analyzes:
1. Customer distribution across segments.
2. Average customer spending.
3. Customer engagement patterns.
4. Most common customer interests.
5. Cluster quality using Silhouette Score.
6. Most common service recommendations.

Actual results are available in the notebook and generated CSV files.

## Project Outputs
- `Day41_Customer_Segmentation_Recommendation.ipynb`
- `Customer_Segmentation_Results.csv`
- `Customer_Segment_Profiles.csv`
- `app.py`

## Conclusion
This project demonstrates how unsupervised machine learning can be applied to customer analytics. K-Means clustering helps identify behavior-based customer groups, while recommendation logic provides relevant learning program and service suggestions.

The project also provides practical experience in feature engineering, PCA, clustering evaluation, and interactive dashboard development.

## Author
Monika Mourya

**Internship:** Veda Technology – Data Science Internship  
**Task:** Customer Segmentation & Service Recommendation System