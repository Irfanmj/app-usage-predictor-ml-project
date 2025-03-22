import pandas as pd
import numpy as np

# Define number of samples
num_samples = 100

# Generate dummy data
data = {
    'Screen_Taps': np.random.randint(5, 20, num_samples),
    'Notifications_Clicked': np.random.randint(0, 5, num_samples),
    'Hour_of_Day': np.random.randint(0, 24, num_samples),
    'Total_Sessions_Today': np.random.randint(1, 10, num_samples),
    'hour': np.random.randint(0, 24, num_samples),
    'day_of_week': np.random.randint(0, 7, num_samples),
    'is_weekend': np.random.randint(0, 2, num_samples),
    'Rolling_Avg_Duration': np.random.uniform(80, 150, num_samples),
    'User_Avg_Duration': np.random.uniform(70, 140, num_samples),
    'User_Total_Duration': np.random.randint(3000, 10000, num_samples),
    'User_Session_Count': np.random.randint(10, 100, num_samples),
    'App_Popularity_Rank': np.random.randint(1, 20, num_samples),
    'Duration_Per_Session': np.random.uniform(80, 130, num_samples),
    'User_ID_Encoded': np.random.randint(1, 50, num_samples),
    'App_Name_Encoded': np.random.randint(1, 20, num_samples),
    'Day_of_Week_Encoded': np.random.randint(0, 6, num_samples),
    'Previous_App_Used_Encoded': np.random.randint(0, 10, num_samples),
}

df = pd.DataFrame(data)

# Generate target variable (Log_Duration) based on some features
df['Log_Duration'] = (
    0.02 * df['Screen_Taps'] +
    0.05 * df['Notifications_Clicked'] +
    0.01 * df['Total_Sessions_Today'] +
    0.03 * df['Rolling_Avg_Duration'] +
    0.02 * df['User_Avg_Duration'] +
    0.001 * df['User_Total_Duration'] +
    0.03 * df['Duration_Per_Session'] +
    np.random.normal(0, 0.5, num_samples)  # add some noise
)

# Round target for simplicity
df['Log_Duration'] = df['Log_Duration'].round(2)

# Save to CSV
df.to_csv("dataset.csv", index=False)
print("✅ dataset.csv generated with", num_samples, "samples.")
