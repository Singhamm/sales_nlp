
import pickle
#import helpers.py
from helpers import preprocess


from flask import Flask, request, app, url_for, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)  #Starting Point

#Load the model and the Count Vectorizer
final_model = pickle.load(open('model.pkl', 'rb'))
count_vect = pickle.load(open('cv.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.form['Notes']
    print(data)
    val = preprocess(data)
    outcome = count_vect.transform([val])
    final_val = outcome.toarray()
    probab_out = final_model.predict_proba(final_val)
    output_f = final_model.predict(final_val)
    print(probab_out)
    if output_f==0:
        return render_template("home.html", prediction_text=f"Candidate is converted and we can connect for further queries")
    else:
        check_val = round(probab_out[0][1]*100,2)
        if check_val>40:
            return render_template("home.html", prediction_text=f"Candidate's closing percentage is: {check_val}%, Sales team should reach")
        elif check_val>30 and check_val<=40:
           return render_template("home.html", prediction_text=f"Candidate's closing percentage is: {check_val}%, Please keep in the database") 
        else:
            return render_template("home.html", prediction_text=f"Candidate's closing percentage is: {check_val}%, Please don't reach further") 

if __name__ =="__main__":
    app.run(debug=True)
