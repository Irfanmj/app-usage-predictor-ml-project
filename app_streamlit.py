import streamlit as st
import pickle
import numpy as np
import math

# Load the model and feature list
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("features_list.pkl", "rb") as f:
    features = pickle.load(f)

# Streamlit app
st.title("📱 App Usage Duration Predictor")

st.markdown("""
This app predicts the estimated app usage duration based on user input. 
Fill in the details below and click **Predict Duration** to get the result.
""")

# Input fields for user data
input_data = []
for feature in features:
    if feature == "Screen_Taps":
        value = st.number_input("How many screen taps?", step=1)
    elif feature == "Notifications_Clicked":
        value = st.number_input("How many notifications were clicked?", step=1)
    elif feature == "Hour_of_Day":
        value = st.number_input("What is the hour of the day? (0-23)", min_value=0, max_value=23, step=1)
    elif feature == "Total_Sessions_Today":
        value = st.number_input("How many sessions did the user have today?", step=1)
    elif feature == "hour":
        value = st.number_input("What is the current hour? (0-23)", min_value=0, max_value=23, step=1)
    elif feature == "day_of_week":
        value = st.number_input("What day of the week is it? (0=Monday, 6=Sunday)", min_value=0, max_value=6, step=1)
    elif feature == "is_weekend":
        value = st.selectbox("Is it a weekend?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    elif feature == "Rolling_Avg_Duration":
        value = st.number_input("What is the rolling average duration of previous sessions?", step=0.01)
    elif feature == "User_Avg_Duration":
        value = st.number_input("What is the user's average session duration?", step=0.01)
    elif feature == "User_Total_Duration":
        value = st.number_input("What is the user's total usage duration?", step=0.01)
    elif feature == "User_Session_Count":
        value = st.number_input("How many sessions has the user had in total?", step=1)
    elif feature == "App_Popularity_Rank":
        value = st.number_input("What is the app's popularity rank?", step=1)
    elif feature == "Duration_Per_Session":
        value = st.number_input("What is the average duration per session?", step=0.01)
    elif feature == "User_ID_Encoded":
        value = st.number_input("What is the encoded User ID?", step=1)
    elif feature == "App_Name_Encoded":
        value = st.number_input("What is the encoded App Name?", step=1)
    elif feature == "Day_of_Week_Encoded":
        value = st.number_input("What is the encoded Day of Week?", step=1)
    elif feature == "Previous_App_Used_Encoded":
        value = st.number_input("What is the encoded value of the previously used app?", step=1)
    else:
        value = st.number_input(f"{feature.replace('_', ' ')}", step=0.01)
    input_data.append(value)

# Predict button
if st.button("Predict Duration"):
    try:
        # Convert input data to numpy array and make prediction
        input_array = np.array(input_data).reshape(1, -1)
        log_prediction = model.predict(input_array)[0]
        duration_minutes = round(math.exp(log_prediction), 2)

        # Display the result
        st.success(f"📊 Estimated app usage duration is approximately **{duration_minutes} minutes**.")
    except Exception as e:
        st.error(f"Error: {str(e)}")