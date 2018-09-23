from flask import Flask, render_template, request
from flask import redirect, url_for
import api

#
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    user_id = request.args.get('user_id')
    if user_id is None:
        url = api.authorize()
        return render_template('index.html', oauth_url=url)
    else:
        response = api.stocks(user_id)
        if response.status_code == 200:
            stocks = response.json()
        return render_template('index.html', stocks=stocks)


@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    response = api.access_tokens(code, state)
    if response.status_code == 201:
        response = api.authenticated_user(response.json()['token'])
        if response.status_code == 200:
            user_id = response.json()['id']
            print(f'user_id: {user_id}')
    # return render_template('index.html')
    return redirect(url_for('index', user_id=user_id))


if __name__ == '__main__':
    app.run()
