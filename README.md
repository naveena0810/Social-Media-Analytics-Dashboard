# 📊 Social Media Sentiment Analysis & Analytics Dashboard

## 📌 Project Overview

The **Social Media Analytics Dashboard** is a data analysis and visualization project designed to explore engagement patterns and sentiment trends in social media posts. The system processes a Twitter dataset and provides interactive insights through a web dashboard built with **Streamlit** and **Plotly**.

The project performs **data cleaning, exploratory data analysis (EDA), sentiment classification, and visualization** to help understand how users interact with posts and what sentiments are expressed over time.

The dashboard allows users to filter data by **date range and sentiment category**, making it easier to analyze patterns such as engagement trends, sentiment distribution, and daily activity.

---

## 🎯 Project Objectives

* Analyze social media posts to identify **sentiment trends**.
* Measure **user engagement metrics** such as likes and retweets.
* Build an **interactive analytics dashboard** for real-time insights.
* Perform **data cleaning and exploratory data analysis (EDA)**.
* Provide clear **visualizations of sentiment and engagement patterns**.

---

## 🧠 Key Features

* 📈 **Interactive Dashboard** for analyzing social media data
* 🧹 **Data Cleaning & Preprocessing** for accurate analysis
* 😊 **Sentiment Analysis** using Natural Language Processing
* 📊 **Dynamic Visualizations** with Plotly
* 📅 **Date Range Filtering** for timeline analysis
* 📊 **Engagement KPI Metrics** (likes, retweets, total posts)

---

## 📂 Project Structure

```
Social-Media-Analytics-Dashboard
│
├── dashboard.py              # Main Streamlit dashboard application
├── explore_dataset.py        # Script for exploratory data analysis
├── twitter_dataset.csv       # Dataset containing social media posts
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── social_media_eda.ipynb    # Jupyter notebook for data exploration
```

---

## ⚙️ Technologies Used

### Programming Language

* Python

### Data Processing

* **Pandas** – Data manipulation and cleaning
* **NumPy** – Numerical computations

### Data Visualization

* **Plotly** – Interactive charts and graphs

### Web Dashboard

* **Streamlit** – Building interactive web apps

### Natural Language Processing

* **TextBlob** – Sentiment analysis of tweets

---

## 🔍 Data Processing Pipeline

### 1️⃣ Data Loading

The dataset containing tweets is loaded using **Pandas**. The system also handles encoding issues automatically.

### 2️⃣ Data Cleaning

The dataset is processed to ensure quality by:

* Removing duplicate records
* Handling missing text values
* Converting timestamps to datetime format

### 3️⃣ Feature Engineering

Additional features are extracted from timestamps such as:

* Date
* Hour
* Day of the week

### 4️⃣ Sentiment Analysis

Each tweet is analyzed using **TextBlob** to determine whether the sentiment is:

* Positive
* Negative
* Neutral

This classification is based on the **polarity score** of the tweet text.

---

## 📊 Dashboard Analytics

The dashboard displays several key insights:

### 📌 Key Performance Indicators (KPIs)

* Total number of posts
* Average likes per post
* Average retweets per post
* Total positive tweets

### 📈 Visualizations

The dashboard includes:

1️⃣ **Sentiment Distribution Pie Chart**

* Shows the proportion of positive, negative, and neutral tweets.

2️⃣ **Daily Engagement Trends Line Chart**

* Displays average likes and retweets over time.

3️⃣ **Sentiment by Day of Week Bar Chart**

* Shows how sentiment varies across different days.

---

## 📊 Dataset Exploration Script

The project also includes a dataset exploration script that performs:

* Dataset structure analysis
* Missing value detection
* Data type inspection
* Statistical summary
* Column value sampling

This script helps understand the dataset before visualization and modeling. 

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/social-media-analytics-dashboard.git
cd social-media-analytics-dashboard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

The required libraries are listed in the project dependency file. 

### 3️⃣ Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will automatically open in your browser.

---

## 📈 Key Insights from Analysis

* Most tweets have **positive or neutral sentiment**, while negative tweets are relatively few.
* Engagement levels (likes and retweets) remain **consistent over time**.
* Tweet activity appears **stable across the monitored time period**.
* Sentiment distribution varies slightly depending on the **day of the week**.

These insights help understand **public opinion and engagement patterns on social media**. 

---

## 📚 Learning Outcomes

Through this project, the following skills were developed:

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Sentiment Analysis using NLP
* Interactive Data Visualization
* Dashboard Development with Streamlit
* Real-world Data Analysis Workflow

---

## 🔮 Future Improvements

Possible future enhancements include:

* Real-time Twitter API integration
* Machine Learning based sentiment models
* Word cloud visualization
* Topic modeling for tweet analysis
* Advanced engagement prediction

---

## 👨‍💻 Author

**Naveena N**

Data Science / Python Enthusiast
Passionate about building data-driven solutions and analytics dashboards.


