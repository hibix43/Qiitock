from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify, session
import qiitainfo
import api
from edit_json import minimum_entries

app = Flask(__name__,
            static_folder='./dist/static',
            template_folder="./dist")
app.secret_key = qiitainfo.SESSION_SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login_url():
    if session.get('user_id') is None:
        return jsonify(login_data={'login_url': api.authorize()})
    else:
        return jsonify(error={'error_msg': 'Already logged'})


@app.route('/stocks/<int:page>')
def users_stocks(page):
    user_id = session.get('user_id')
    token = session.get('token')
    if user_id is None or token is None:
        return jsonify(error={'error_msg': 'Please login'})
    else:
        response = api.stocks(user_id, page=page, token=token)
        if response.status_code == 200:
            stocks = response.json()
            # JSONを最低限の項目のみに書き換える
            stocks = minimum_entries(stocks)
            return jsonify(stocks=stocks)
        else:
            return jsonify(error={'error_msg': 'Users stocks not found'})


@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    response = api.access_tokens(code, state)
    if response.status_code == 201:
        token = response.json()['token']
        session['token'] = token
        response = api.authenticated_user(token)
        if response.status_code == 200:
            session['user_id'] = response.json()['id']
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
