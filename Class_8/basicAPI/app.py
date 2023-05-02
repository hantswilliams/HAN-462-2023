from flask import Flask
import pandas as pd

app = Flask(__name__)


# endpoints 
@app.route('/')
def default_home():
    return 'API Endpoint from Hants Williams'

#### RETRIEVING 

@app.route('/api/v1/students')
def students():
    df = pd.read_csv('datafile.csv')
    return df.to_json(orient='records')

@app.route('/api/v1/students/<int:number>')
def students_limit(number):
    df = pd.read_csv('datafile.csv')
    df = df.head(number)
    return df.to_json(orient='records')




##### SEARCHING #####

@app.route('/api/v1/students/search/lastname/<string:lastname>')
def students_search_lastname(lastname):
    df = pd.read_csv('datafile.csv')
    df.columns = df.columns.str.replace(' ', '_')
    df = df[df['Last_Name'].str.contains(lastname)]
    return df.to_json(orient='records')

@app.route('/api/v1/students/search/firstname/<string:firstname>')
def students_search_firstname(firstname):
    df = pd.read_csv('datafile.csv')
    df.columns = df.columns.str.replace(' ', '_')
    df = df[df['First_Name'].str.contains(firstname)]
    return df.to_json(orient='records')





if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)