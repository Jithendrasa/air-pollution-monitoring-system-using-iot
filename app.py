from flask import Flask, render_template, jsonify
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the trained machine learning model
# Replace with your model loading code
model = RandomForestClassifier()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # Generate synthetic sensor readings for demonstration
    mq135_ppm = np.random.uniform(low=0, high=200)
    mq6_ppm = np.random.uniform(low=0, high=300)

    # Make a prediction using the trained model
    # Replace with your actual prediction logic
    new_data_point = np.array([[mq135_ppm, mq6_ppm]])
    predicted_air_quality = model.predict(new_data_point)[0]

    # Prepare the data to be sent to the frontend
    data = {
        'mq135_ppm': mq135_ppm,
        'mq6_ppm': mq6_ppm,
        'predicted_air_quality': predicted_air_quality
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
