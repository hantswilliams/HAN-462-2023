from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def default_home():
    return 'API Endpoint from Hants Williams'

# if __name__ == '__main__':
#     app.run(debug=True, host='localhost', port=80)