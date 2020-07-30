#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np 
import pandas as pd
import flask
from flask import Flask , request, jsonify
import json
import pickle


# In[4]:


app = Flask(__name__)
model = pickle.load(open('Engine.pkl', 'rb'))


# In[7]:


@app.route('/predict', methods = ['POST'])
def predict():
    input_data = pd.read_csv(request.files.get("input_file"))
    prediction = model.predict(input_data)
    response = json.dump(prediction)
    return response


# In[ ]:


if __name__ == "__main__":
    app.run()

