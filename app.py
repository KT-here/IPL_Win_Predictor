import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('ipl_win_predictor.pkl')

# Title
st.title("🏏 IPL Win Probability Predictor")

# Team and City Options
teams = ['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders',
         'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']

cities = ['Mumbai', 'Kolkata', 'Chennai', 'Delhi', 'Bangalore', 'Hyderabad', 'Jaipur', 'Ahmedabad']

# Input Fields
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", [team for team in teams if team != batting_team])
city = st.selectbox("City", cities)

target = st.number_input("Target Score", min_value=50)
score = st.number_input("Current Score", min_value=0, max_value=int(target))
wickets = st.slider("Wickets Remaining", 0, 10, 10)
overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)

# Calculate additional features
runs_left = target - score
balls_left = 120 - int(overs * 6)
crr = score / overs if overs > 0 else 0
rrr = (runs_left * 6 / balls_left) if balls_left > 0 else 0

# Predict
if st.button("Predict Win Probability"):
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    probability = model.predict_proba(input_df)[0][1]
    st.success(f"🏆 Win Probability for {batting_team}: {probability * 100:.2f}%")
