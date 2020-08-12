#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np 
import pandas as pd
import flask
from flask import Flask , request, jsonify
import json
import pickle




app = Flask(__name__)
model = pickle.load(open('Engine.pkl', 'rb'))

@app.route('/')
def form():
	return '''
	<form method="POST" action="predict">
	<h1>Enter the files for the prediction.</h1>
	<input type="number" name="meterread" placeholder="meterread" required /> 
	<input type="number" name="FT_IR_Water" placeholder="FT-IR Water" required />
	<input type="submit" name="Submit" />
	</form>
	'''
@app.route('/predict', methods = ['GET','POST'])
def predict():
    meterread = request.form.get("meterread")
    FT_IR_Water = request.form.get("FT_IR_Water")
    input_data = np.array([[meterread, FT_IR_Water]])
    prediction = model.predict(input_data)
    #response = json.dump(prediction)
    return '<h1>The predicted time of Engine failure is {}</h1>'.format(prediction)




if __name__ == "__main__":
    app.run(debug = True)

