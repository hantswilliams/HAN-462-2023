from flask import Flask
from flask import render_template

# here we are going to modify to set the folders that contain our static files and templates
app = Flask(__name__)


"""
In Python, a decorator is a function that takes another function as an argument, 
and extends or modifies its behavior without changing its source code. A decorator 
is denoted by the @ symbol followed by the name of the decorator function, which is 
placed above the function being decorated. In the context of Flask, the @app decorator 
is used to define a Flask application object, which is an instance of the Flask 
class that represents the web application. The @app decorator is used to 
decorate functions that define the routes of the application, i.e., the URLs that the
application will respond to.
"""


@app.route('/')
def hello_world():
    return 'Hello world!'

# exampe of how to take a argument from the url
@app.route('/hello/<name>') 
def hello_name(name):
    return 'Hello %s!' % name

# example of how to take a argument from the url and return a number
@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return '%d + %d = %d' % (x, y, x+y)

# example of how to set a new HTML file to be the default page
@app.route('/index')
def index():
    return render_template('index.html')



## Note, if you want to run this app with the command `python app.py`, you need to add the following line to the end of the file
## so it can execute and stay running....
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)

"""
__name__ == '__main__': line in a Python script is used to ensure that the code block 
following it is only executed if the script is being run as the main program, 
rather than being imported as a module into another program
"""