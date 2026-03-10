import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob

# --- Configuration and Data Loading ---

# 1. Set page title and layout
st.set_page_config(layout="wide", page_title="Social Media Analytics Dashboard")

DATASET_FILE = 'twitter_dataset.csv' 

# Function to load and clean the data (Caching prevents reloading data on every interaction)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(DATASET_FILE, encoding='latin-1', on_bad_lines='skip')
    except:
        st.error(f"Error loading file: {DATASET_FILE}. Check the path.")
        return pd.DataFrame() # Return empty dataframe on failure
    
    # Cleaning and Feature Engineering (from Day 3/4)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df.dropna(subset=['Text'], inplace=True)
    df.drop_duplicates(inplace=True)
    
    df['Date'] = df['Timestamp'].dt.date
    df['Hour'] = df['Timestamp'].dt.hour
    df['DayOfWeek'] = df['Timestamp'].dt.day_name()
    return df

# Function for Sentiment Analysis (from Day 5)
def get_sentiment(text):
    try:
        analysis = TextBlob(str(text))
        if analysis.sentiment.polarity > 0.1:
            return 'Positive'
        elif analysis.sentiment.polarity < -0.1:
            return 'Negative'
        else:
            return 'Neutral'
    except:
        return 'Neutral'

# Load the data
df_full = load_data()
if df_full.empty:
    st.stop()

# Perform Sentiment Analysis (only once)
if 'Sentiment' not in df_full.columns:
    df_full['Sentiment'] = df_full['Text'].apply(get_sentiment)


# --- Dashboard Layout and Filters ---

st.title('📊 Social Media Analytics Dashboard')

# Sidebar Filters
st.sidebar.header('Filter Data')

# Date Filter
date_list = sorted(df_full['Date'].unique())
start_date, end_date = st.sidebar.select_slider(
    'Select Date Range',
    options=date_list,
    value=(date_list[0], date_list[-1])
)

# Sentiment Filter
sentiment_options = ['All'] + df_full['Sentiment'].unique().tolist()
selected_sentiment = st.sidebar.selectbox('Filter by Sentiment', sentiment_options)

# Apply filters
df = df_full[df_full['Date'].between(start_date, end_date)]
if selected_sentiment != 'All':
    df = df[df['Sentiment'] == selected_sentiment]


# --- 3. Key Performance Indicators (KPIs) ---

total_posts = len(df)
avg_likes = df['Likes'].mean() if not df.empty else 0
avg_retweets = df['Retweets'].mean() if not df.empty else 0
total_pos = df[df['Sentiment'] == 'Positive'].shape[0] if not df.empty else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Posts", f"{total_posts:,}")
col2.metric("Avg. Likes per Post", f"{avg_likes:.1f}")
col3.metric("Avg. Retweets per Post", f"{avg_retweets:.1f}")
col4.metric("Positive Tweets", f"{total_pos:,}")


# --- 4. Visualizations (using your Plotly code) ---

st.header("Key Insights & Trends")

col_left, col_right = st.columns([1, 2])

# LEFT COLUMN: Sentiment Distribution Pie Chart
with col_left:
    st.subheader("Overall Sentiment Distribution")
    if not df.empty:
        sentiment_counts = df['Sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']

        fig_pie = px.pie(
            sentiment_counts, 
            values='Count', 
            names='Sentiment', 
            color='Sentiment',
            color_discrete_map={'Positive':'#1f77b4', 'Negative':'#d62728', 'Neutral':'#ff7f0e'}
        )
        fig_pie.update_traces(textinfo='percent', pull=[0, 0, 0.1])
        st.plotly_chart(fig_pie, use_container_width=True)

# RIGHT COLUMN: Engagement Trends Line Chart
with col_right:
    st.subheader("Daily Engagement Trends")
    if not df.empty:
        daily_engagement = df.groupby('Date')[['Likes', 'Retweets']].mean().reset_index()
        fig_line = px.line(
            daily_engagement, 
            x='Date', 
            y=['Likes', 'Retweets'], 
            title='Average Daily Engagement (Likes & Retweets)',
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)


# BOTTOM ROW: Sentiment by Day Bar Chart
st.subheader("Sentiment Analysis by Day of Week")
if not df.empty:
    sentiment_by_day = df.groupby('DayOfWeek')['Sentiment'].value_counts().unstack(fill_value=0)
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sentiment_by_day = sentiment_by_day.reindex(day_order)

    fig_bar = px.bar(
        sentiment_by_day, 
        x=sentiment_by_day.index, 
        y=sentiment_by_day.columns, 
        labels={'x':'Day of Week', 'value':'Total Count'},
        color_discrete_map={'Positive':'#1f77b4', 'Negative':'#d62728', 'Neutral':'#ff7f0e'}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Run this cell (Shift + Enter)