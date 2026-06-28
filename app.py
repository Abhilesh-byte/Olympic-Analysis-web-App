import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

import preprocessor
import helper

# ---------------- Page config ----------------
st.set_page_config(page_title='Olympics Analysis', page_icon='🏅', layout='wide')

# ---------------- Load data ----------------
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df, region_df)

# ---------------- Sidebar ----------------
st.sidebar.image(
    'https://upload.wikimedia.org/wikipedia/commons/5/5c/Olympic_rings_without_rims.svg',
    width=120
)
st.sidebar.title('Olympics Analysis')

user_menu = st.sidebar.radio(
    'Select an Option',
    (
        'Medal Tally',
        'Overall Analysis',
        'Country-wise Analysis',
        'Athlete wise Analysis'
    )
)

# =====================================================================
# 1. MEDAL TALLY
# =====================================================================
if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox('Select Year', years)
    selected_country = st.sidebar.selectbox('Select Country', country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Tally')
    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.title(f'Medal Tally in {selected_year} Olympics')
    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.title(f'{selected_country} Overall Performance')
    else:
        st.title(f'{selected_country} performance in {selected_year} Olympics')

    st.table(medal_tally)

# =====================================================================
# 2. OVERALL ANALYSIS
# =====================================================================
if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title('Top Statistics')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athletes')
        st.title(athletes)

    st.title('Participating Nations over the Years')
    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x='Edition', y='region')
    st.plotly_chart(fig)

    st.title('Events over the Years')
    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x='Edition', y='Event')
    st.plotly_chart(fig)

    st.title('Athletes over the Years')
    athletes_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athletes_over_time, x='Edition', y='Name')
    st.plotly_chart(fig)

    st.title('No. of Events over time (every Sport)')
    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(
        x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
        annot=True
    )
    st.pyplot(fig)

    st.title('Most Successful Athletes')
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df, selected_sport)
    st.table(x)

# =====================================================================
# 3. COUNTRY-WISE ANALYSIS
# =====================================================================
if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country', country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country)
    st.title(f'{selected_country} Medal Tally over the Years')
    if not country_df.empty:
        fig = px.line(country_df, x='Year', y='Medal')
        st.plotly_chart(fig)
    else:
        st.info('No medal data available for this country.')

    st.title(f'{selected_country} excels in the following sports')
    pivot_table = helper.country_event_heatmap(df, selected_country)
    if not pivot_table.empty:
        fig, ax = plt.subplots(figsize=(20, 20))
        ax = sns.heatmap(pivot_table, annot=True)
        st.pyplot(fig)
    else:
        st.info('No heatmap data available for this country.')

    st.title(f'Top 10 Athletes of {selected_country}')
    top10_df = helper.most_successful_countrywise(df, selected_country)
    st.table(top10_df)

# =====================================================================
# 4. ATHLETE WISE ANALYSIS
# =====================================================================
if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    st.title('Distribution of Age')
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = px.histogram(
        pd.concat([
            pd.DataFrame({'Age': x1, 'Group': 'Overall Age'}),
            pd.DataFrame({'Age': x2, 'Group': 'Gold Medalist'}),
            pd.DataFrame({'Age': x3, 'Group': 'Silver Medalist'}),
            pd.DataFrame({'Age': x4, 'Group': 'Bronze Medalist'}),
        ]),
        x='Age', color='Group', barmode='overlay', nbins=50
    )
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)

    st.title('Men vs Women Participation Over the Years')
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)