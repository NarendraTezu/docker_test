## flask app for hellow world 

from crypt import methods
from curses import meta
from flask import Flask
from importlib_metadata import method_cache
import numpy as np
import pandas as pd 


app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World Narendra"



if __name__=="__main__":
    app.run(debug=True)