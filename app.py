from flask import Flask, url_for, render_template
#from util.db_util import add_user

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')
