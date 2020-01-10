from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.run(host='0.0.0.0', port=environ.get('PORT'))
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()