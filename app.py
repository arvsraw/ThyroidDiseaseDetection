from flask import Flask, flash, redirect, render_template, request, app, url_for
import numpy as np
import pandas as pd
import pickle
import os
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

model = pickle.load(open('saved_dectree.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    print("home page works")
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    values = []
    entries = request.form
    for key,value in entries.items():
        values.append(value)
    print(values)
    print('\n')
    values = np.array(pd.to_numeric(values)).reshape(1,-1)
    data = scaler.transform(values)


    print(data)

    res = model.predict(data)
    if res==1:
        flash("Result of Thyroid Disease Prediction is: POSITIVE")
    else:
        flash("Result of Thyroid Disease Prediction is: NEGATIVE")

    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)