from flask import current_app as app
from flask import redirect, render_template, url_for, request
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from commonregex import CommonRegex
import re
import time
import os

airport_data = pd.read_csv('airport_data.csv')

# US only

airport_data = airport_data[airport_data['country']=='United States']

airport_data = airport_data[airport_data['airport_code']!="\\N"]
airport_data = airport_data[airport_data['airport_code'].notna()]

airport_data['combined'] = airport_data['city']+"("+airport_data['airport_code']+")"

airport_data = airport_data.sort_values('combined')

airport_list = airport_data['combined']



@app.route("/",methods=("GET", "POST"))
def home():
    return render_template("index.html",airport_list = airport_list)