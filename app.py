from flask import Flask
from util.db_util import add_user

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello</p>"

