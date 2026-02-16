from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Initialize Flask
app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Home page (serves your HTML UI)
@app.route('/')
def home():
    return render_template('index.html')

# Predict API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = ["CO(GT)", "NOx(GT)", "PT08.S5(O3)", "T", "RH", "AH"]
        values = [float(data.get(f, 0)) for f in features]
        arr = np.array([values])
        prediction = model.predict(arr)[0]
        return jsonify({
            "status": "success",
            "predicted_NO2": round(float(prediction), 2)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
