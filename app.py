from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import pandas as pd

app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file =request.form['upload-file']
        data = pd.read_excel(file)
        return render_template('data.html', data=data.to_html())

    
if __name__ == '__main__':
    app.run(debug=True)
