from flask import Flask
from flask import render_template, redirect, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_page():
    return render_template("index.html", title='EduVerse | Home')


if __name__ == "__main__":
    app.run(debug=True)