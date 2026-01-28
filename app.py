import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="AI Academic Insight Dashboard",
    layout="wide"
)

st.title("📊 AI Academic Insight Dashboard for Faculty")

# Load data
df = pd.read_csv("phase2_ai_output.csv")

# Sidebar filters
st.sidebar.header("Filters")
selected_class = st.sidebar.selectbox(
    "Select Class",
    df["class"].unique()
)

filtered_df = df[df["class"] == selected_class]

# KPIs
st.subheader("📌 Class Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Attendance",
    f"{filtered_df['attendance_pct'].mean():.1f}%"
)

col2.metric(
    "At Risk Students",
    filtered_df[filtered_df["ai_prediction"] == "At Risk"].shape[0]
)

col3.metric(
    "Total Students",
    filtered_df["student_id"].nunique()
)

# Risk table
st.subheader("⚠️ Students Needing Attention")

risk_df = filtered_df[filtered_df["ai_prediction"] != "Safe"]

st.dataframe(
    risk_df[[
        "student_name",
        "ai_prediction",
        "risk_reason"
    ]]
)

# Student drill-down
st.subheader("🔍 Student Detail View")

student = st.selectbox(
    "Select Student",
    filtered_df["student_name"].unique()
)

student_data = filtered_df[
    filtered_df["student_name"] == student
]

st.write(
    student_data[[
        "attendance_pct",
        "internal_1",
        "internal_2",
        "assignment_delay",
        "ai_prediction",
        "risk_reason"
    ]]
)
