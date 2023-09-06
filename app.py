import json
from flask import Flask, request, jsonify, url_for, render_template
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load the pre-trained model using 'rb' mode
model_name = 'ET_Model.pkl'
with open(model_name, 'rb') as model_file:
    ET_Model = joblib.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = ET_Model.predict(final_features)

    output = round(prediction[0], 1)

    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

