import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    "Screen_Taps": 10,
    "Notifications_Clicked": 3,
    "Hour_of_Day": 14,
    "Total_Sessions_Today": 5,
    "hour": 14,
    "day_of_week": 2,
    "is_weekend": 0,
    "Rolling_Avg_Duration": 120.5,
    "User_Avg_Duration": 110.2,
    "User_Total_Duration": 5400,
    "User_Session_Count": 50,
    "App_Popularity_Rank": 12,
    "Duration_Per_Session": 108,
    "User_ID_Encoded": 21,
    "App_Name_Encoded": 7,
    "Day_of_Week_Encoded": 3,
    "Previous_App_Used_Encoded": 4
}

response = requests.post(url, json=data)
print("Response from API:", response.json())
