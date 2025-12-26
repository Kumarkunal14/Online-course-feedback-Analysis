import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Feedback Analysis", layout="centered")

# Title
st.title("📊 Online Course Student Feedback Analysis")
st.markdown("**Minor Project – Pandas**")

# Upload CSV
uploaded_file = st.file_uploader("Upload Kaggle Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset loaded successfully!")

        # Preview
        st.subheader("📁 Dataset Preview")
        st.dataframe(df.head())

        # Select rating column
        st.subheader("⚙ Select Rating Column")
        rating_col = st.selectbox("Choose Rating Column", df.columns)

        # Descriptive statistics
        st.subheader("📈 Descriptive Statistics")
        st.write(df[rating_col].describe())

        # Rating distribution
        st.subheader("⭐ Rating Distribution")
        rating_counts = df[rating_col].value_counts().sort_index()

        fig, ax = plt.subplots()
        ax.bar(rating_counts.index, rating_counts.values)
        ax.set_xlabel("Rating")
        ax.set_ylabel("Number of Students")
        ax.set_title("Rating Distribution")
        st.pyplot(fig)

        # Satisfaction logic
        def satisfaction(r):
            if r >= 4:
                return "High"
            elif r == 3:
                return "Medium"
            else:
                return "Low"

        df["Satisfaction"] = df[rating_col].apply(satisfaction)

        # Satisfaction insights
        st.subheader("😊 Satisfaction Insights")
        st.write(df["Satisfaction"].value_counts())

        # Satisfaction chart
        fig2, ax2 = plt.subplots()
        df["Satisfaction"].value_counts().plot(kind="bar", ax=ax2)
        ax2.set_xlabel("Satisfaction Level")
        ax2.set_ylabel("Number of Students")
        ax2.set_title("Student Satisfaction Analysis")
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error: {e}")
