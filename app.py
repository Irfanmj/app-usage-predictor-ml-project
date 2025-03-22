from flask import Flask, request, render_template_string
import pickle
import numpy as np
import math

# Load model and feature list
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("features_list.pkl", "rb") as f:
    features = pickle.load(f)

app = Flask(__name__)

# HTML Template with light blue styling and user-friendly form labels
template = """
<!DOCTYPE html>
<html>
<head>
    <title>App Usage Duration Predictor</title>
    <style>
        body {
            background-color: #E3F2FD; /* Light blue background */
            color: #0D47A1; /* Dark blue text */
            font-family: Arial, sans-serif;
        }
        .container {
            width: 60%%;
            margin: auto;
            padding: 30px;
            background-color: #FFFFFF; /* White container background */
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #0D47A1; /* Dark blue heading */
        }
        form label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
            color: #0D47A1; /* Dark blue labels */
        }
        input, select {
            width: 100%%;
            padding: 10px;
            margin-top: 5px;
            background-color: #FFFFFF; /* White input background */
            color: #0D47A1; /* Dark blue text */
            border: 1px solid #90CAF9; /* Light blue border */
            border-radius: 5px;
        }
        input[type=submit] {
            margin-top: 20px;
            background-color: #0D47A1; /* Dark blue button background */
            color: #FFFFFF; /* White button text */
            cursor: pointer;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            padding: 10px;
        }
        input[type=submit]:hover {
            background-color: #1565C0; /* Slightly lighter blue on hover */
        }
        .result {
            margin-top: 30px;
            padding: 15px;
            background-color: #BBDEFB; /* Light blue result background */
            color: #0D47A1; /* Dark blue text */
            border-radius: 8px;
            font-size: 18px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📱 App Usage Duration Predictor</h1>
        <form method="post">
            <label>1. How many times did the user tap the screen?</label>
            <input type="number" name="Screen_Taps" required>

            <label>2. How many times did the user click on notifications?</label>
            <input type="number" name="Notifications_Clicked" required>

            <label>3. What is the hour of the day? (0-23)</label>
            <input type="number" name="Hour_of_Day" min="0" max="23" required>

            <label>4. How many sessions did the user have today?</label>
            <input type="number" name="Total_Sessions_Today" required>

            <label>5. What is the current hour? (0-23)</label>
            <input type="number" name="hour" min="0" max="23" required>

            <label>6. What day of the week is it? (0=Monday, 6=Sunday)</label>
            <input type="number" name="day_of_week" min="0" max="6" required>

            <label>7. Is it a weekend? (0=No, 1=Yes)</label>
            <select name="is_weekend">
                <option value="0">No</option>
                <option value="1">Yes</option>
            </select>

            <label>8. What is the rolling average duration of previous sessions?</label>
            <input type="number" step="0.01" name="Rolling_Avg_Duration" required>

            <label>9. What is the user's average session duration?</label>
            <input type="number" step="0.01" name="User_Avg_Duration" required>

            <label>10. What is the user's total usage duration?</label>
            <input type="number" step="0.01" name="User_Total_Duration" required>

            <label>11. How many sessions has the user had in total?</label>
            <input type="number" name="User_Session_Count" required>

            <label>12. What is the app's popularity rank?</label>
            <input type="number" name="App_Popularity_Rank" required>

            <label>13. What is the average duration per session?</label>
            <input type="number" step="0.01" name="Duration_Per_Session" required>

            <label>14. What is the encoded User ID?</label>
            <input type="number" name="User_ID_Encoded" required>

            <label>15. What is the encoded App Name?</label>
            <input type="number" name="App_Name_Encoded" required>

            <label>16. What is the encoded Day of Week?</label>
            <input type="number" name="Day_of_Week_Encoded" required>

            <label>17. What is the encoded value of the previously used app?</label>
            <input type="number" name="Previous_App_Used_Encoded" required>

            <input type="submit" value="Predict Duration">
        </form>
        {% if prediction %}
            <div class="result">
                📊 Estimated app usage duration is approximately <strong>{{ prediction }} minutes</strong>.
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            input_data = [float(request.form.get(feature, 0)) for feature in features]
            input_array = np.array(input_data).reshape(1, -1)
            log_prediction = model.predict(input_array)[0]
            duration_minutes = round(math.exp(log_prediction), 2)
            prediction = duration_minutes
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template_string(template, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
