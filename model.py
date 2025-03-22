# model.py
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Load dataset
df = pd.read_csv("dataset_v2.csv")

# Separate features and target
features_list = [
    'Screen_Taps', 'Notifications_Clicked', 'Hour_of_Day', 'Total_Sessions_Today', 'hour',
    'day_of_week', 'is_weekend', 'Rolling_Avg_Duration', 'User_Avg_Duration',
    'User_Total_Duration', 'User_Session_Count', 'App_Popularity_Rank',
    'Duration_Per_Session', 'User_ID_Encoded', 'App_Name_Encoded',
    'Day_of_Week_Encoded', 'Previous_App_Used_Encoded'
]

X = df[features_list]
y = df["Log_Duration"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model Trained")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R² Score: {r2:.4f}")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save features list
with open("features_list.pkl", "wb") as f:
    pickle.dump(features_list, f)

print("✅ model.pkl & features_list.pkl saved!")
