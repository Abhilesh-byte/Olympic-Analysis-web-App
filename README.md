# 🏅 Olympic Analysis Web App

An interactive web application for exploring 120 years of Olympic history (1896–2016), built with **Python** and **Streamlit**. The app analyzes athlete, country, and medal data to surface trends in participation, performance, and growth across editions of the Games.

## 🔗 Live Demo

[Add your Streamlit Cloud app link here]

## 📊 Features

- **Medal Tally** — Filter medal counts by year and/or country to see gold, silver, bronze, and total medal standings.
- **Overall Analysis** — High-level statistics across all Olympic editions: number of editions, host cities, nations, events, and athletes, plus year-over-year trends in participation.
- **Country-wise Analysis** — Drill into a specific country's medal tally over time and identify its top-performing athletes by sport.
- **Athlete-wise Analysis** — Explore age distribution, height/weight trends, and performance patterns of medalists across different sports.

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — web app framework
- **Pandas** — data preprocessing and analysis
- **Matplotlib / Seaborn** — data visualization
- **Plotly** — interactive charts

## 📁 Project Structure

```
Olympic-Analysis-web-App/
├── app.py                # Main Streamlit application (UI and page routing)
├── preprocessor.py        # Data cleaning and preprocessing logic
├── helper.py              # Helper functions for analysis and aggregation
├── athlete_events.csv      # Olympic athlete and event dataset (1896–2016)
├── noc_regions.csv         # NOC (National Olympic Committee) to country/region mapping
├── requirements.txt        # Python dependencies
├── Procfile                # Process file for deployment (e.g. Heroku)
├── setup.sh                # Environment setup script for deployment
└── Olympic.png             # App banner/logo image
```

## 📂 Dataset

This project uses the [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) dataset from Kaggle, which includes:

- **athlete_events.csv** — One row per athlete per event, including name, sex, age, height, weight, team, NOC, year, season, city, sport, event, and medal.
- **noc_regions.csv** — Maps NOC codes to country/region names for cleaner country-level analysis.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Abhilesh-byte/Olympic-Analysis-web-App.git
   cd Olympic-Analysis-web-App
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   streamlit run app.py
   ```

5. Open the URL shown in your terminal (typically `http://localhost:8501`) in your browser.

## ☁️ Deployment

This app is designed for deployment on [Streamlit Community Cloud](https://streamlit.io/cloud). To deploy your own copy:

1. Push the repository to GitHub.
2. Sign in to Streamlit Community Cloud and click **"New app"**.
3. Select this repository, branch (`master`), and set the main file path to `app.py`.
4. Deploy.

> **Note:** Make sure `requirements.txt` lists every package imported in `app.py`, `helper.py`, and `preprocessor.py` (e.g. `streamlit`, `pandas`, `matplotlib`, `seaborn`, `plotly`), and that CSV file paths in the code are relative paths, since Streamlit Cloud's file system differs from a local machine.

## 🙋 Author

**Abhilesh**
Final-year B.Tech (IT) student | Aspiring Data Analyst / Data Scientist

- GitHub: [@Abhilesh-byte](https://github.com/Abhilesh-byte)

## 📄 License

This project is open source and available for learning purposes.# Olympic-Analysis-web-App
