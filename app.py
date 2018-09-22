from flask import Flask, render_template, request
from flask import redirect, url_for
import api

#
app = Flask(__name__)


@app.route('/', methods=['GET'])
def login():
    url = api.oauth_url()
    return render_template('index.html', oauth_url=url)


@app.route('/callback', methods=['GET'])
def main():
    # URL=>code,state
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
