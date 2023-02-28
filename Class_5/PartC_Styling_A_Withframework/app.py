from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('p1_homepage_replicaof_p2manualCSS.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('p2_homepage_withBootstrapedStyled.html')

@app.route('/bootstrap2')
def template():
    return render_template('starter_template.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
