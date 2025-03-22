import pickle

features_list = [
    'Screen_Taps',
    'Notifications_Clicked',
    'Hour_of_Day',
    'Total_Sessions_Today',
    'hour',
    'day_of_week',
    'is_weekend',
    'Rolling_Avg_Duration',
    'User_Avg_Duration',
    'User_Total_Duration',
    'User_Session_Count',
    'App_Popularity_Rank',
    'Duration_Per_Session',
    'User_ID_Encoded',
    'App_Name_Encoded',
    'Day_of_Week_Encoded',
    'Previous_App_Used_Encoded'
]

with open("features_list.pkl", "wb") as f:
    pickle.dump(features_list, f)

print("✅ features_list.pkl created!")
