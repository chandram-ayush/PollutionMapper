from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
from joblib import dump, load
import os
import pickle

app = Flask(__name__,template_folder='template')
model_file= 'random_forest_model_15years_181_.joblib'
if os.path.exists(model_file):
    # Load the model
    model = load(model_file)
    print("Model loaded successfully.")

@app.route("/index", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET', 'POST'])
@cross_origin()
def predict():
    global model
    if request.method == "POST":
        # DATE
        date = request.form['date']
        month = int(str(date)[5:7])
        print(month)

        # lat
        lat = float(request.form['lat'])

        # lon
        lon = float(request.form['lon'])
        u10 = float(request.form['10u'])
        v10 = float(request.form['10v'])
        si10 = float(request.form['si10'])
        t2m = float(request.form['t2m'])
        hcc = float(request.form['hcc'])
        lcc = float(request.form['lcc'])
        tcc = float(request.form['tcc'])
        tco3 = float(request.form['tco3'])
        tcwv = float(request.form['tcwv'])
        tp = float(request.form['tp'])
        cp = float(request.form['cp'])
        msl = float(request.form['msl'])
        rsn = float(request.form['rsn'])
        sf = float(request.form['sf'])



        input_lst = [lat, lon, u10, v10, si10,t2m,cp, hcc, lcc, msl, rsn, sf, tcc, tco3, tcwv, tp]
        for i in range(12):
            if month == i:
                input_lst.append(1)
            else:
                input_lst.append(0)
        pred = model.predict([input_lst])  # Get the first prediction

        # # Pass the prediction value to the template
        return render_template("predict.html", prediction=pred)

    return render_template("predict.html")

if __name__ == '__main__':
    app.run(debug=True)
