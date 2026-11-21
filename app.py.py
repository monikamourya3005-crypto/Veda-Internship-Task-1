
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

st.title("Customer Segmentation & Service Recommendation System")

st.write(
    "Explore customer behavior, segments and personalized recommendations."
)

df = pd.read_csv("Customer_Segmentation_Results.csv")

st.sidebar.header("Filters")

segments = st.sidebar.multiselect(
    "Select Customer Segment",
    df["Customer_Segment"].unique(),
    default=df["Customer_Segment"].unique()
)

filtered_df = df[df["Customer_Segment"].isin(segments)]

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(filtered_df))

col2.metric(
    "Average Monthly Spending",
    round(filtered_df["Monthly_Spending"].mean(), 2)
)

col3.metric(
    "Average Engagement",
    round(filtered_df["Engagement_Score"].mean(), 2)
)

st.subheader("Customer Segment Distribution")

segment_counts = filtered_df["Customer_Segment"].value_counts()
st.bar_chart(segment_counts)

st.subheader("Customer Interest Distribution")

interest_counts = filtered_df["Interest"].value_counts()
st.bar_chart(interest_counts)

st.subheader("Customer Recommendations")

display_columns = [
    "Customer_ID",
    "Interest",
    "Customer_Segment",
    "Recommended_Service"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True
)

st.subheader("Customer Segment Profiles")

profiles = filtered_df.groupby("Customer_Segment")[
    ["Engagement_Score", "Monthly_Spending",
     "Interactions", "Course_Completion_Rate"]
].mean().round(2)

st.dataframe(profiles, use_container_width=True)
