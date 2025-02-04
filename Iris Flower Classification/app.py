from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("iris_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return "Iris Classification API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['features']  # Expecting JSON input: {"features": [5.1, 3.5, 1.4, 0.2]}
        data = np.array(data).reshape(1, -1)  # Convert to 2D array
        data = scaler.transform(data)  # Apply scaling

        prediction = model.predict(data)[0]
        species = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}[prediction]

        return jsonify({"prediction": species})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
