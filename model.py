import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

import joblib
import urllib.request
import traceback

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:/Users/mouni/Desktop/zomatobanglore.csv')

# Exclude the URL column (assuming it's in column 0) from the features
X = df.iloc[:, [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]]  # Exclude the URL column (column 0)

y = df['rate']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

# Preparing Extra Tree Regression
from sklearn.ensemble import ExtraTreesRegressor
ET_Model = ExtraTreesRegressor(n_estimators=120)
ET_Model.fit(X_train, y_train)
y_predict = ET_Model.predict(X_test)

import joblib

# Save the model using 'wb' mode
model_name = 'ET_Model.pkl'
with open(model_name, 'wb') as model_file:
    joblib.dump(ET_Model, model_file)

# Load the saved model using 'rb' mode
with open(model_name, 'rb') as model_file:
    loaded_model = joblib.load(model_file)
    





# Predict using the loaded model (not the original ET_Model)
y_predict=loaded_model.predict(X_test)
   