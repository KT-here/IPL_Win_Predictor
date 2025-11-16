# 🏏 IPL Win Probability Predictor

This project predicts the probability of a team winning an IPL match in real time based on current match conditions. Built using Python, Streamlit, Logistic Regression, and deployed via Streamlit Cloud.

---

## 📌 Features

- Trained on historical IPL match data (matches & deliveries dataset)
- Real-time win prediction based on:
  - Batting/Bowling Team
  - City
  - Runs Left
  - Balls Left
  - Wickets Remaining
  - Target Score
  - Current and Required Run Rates
- Deployed as an interactive web app using Streamlit

---

## 🔧 Tech Stack

- Python 3.10
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit
- Anaconda (for environment management)
- Git + GitHub
- Streamlit Cloud (for deployment)

---

## 📁 Project Structure
IPL_Win_Predictor/
│
├── app.py # Streamlit web app
├── IPL.ipynp # Model training script
├── ipl_win_predictor.pkl # Saved trained model
├── matches.csv # IPL match-level data
├── deliveries.csv # Ball-by-ball data
├── requirements.txt # Project dependencies
├── README.md # You're reading this!
└── .gitignore # Ignored files


# 🌐 Live App (If Deployed)
[Click to open the app]([https://iplwinpredictor-7uxy9xubupbktrbyima9ws.streamlit.app/])
