import qiitainfo
import proxies
from urllib import parse
from json import dumps
from requests import get, post, Response


headers = {
    'Authorization': 'Bearer ',
    'Content-Type': 'application/json',
}


def authorize():
    url = 'https://qiita.com/api/v2/oauth/authorize'
    params = {
        'client_id': qiitainfo.ID,
        'scope': 'read_qiita',
        'state': qiitainfo.STATE,
    }
    return url + '?' + parse.urlencode(params)


def access_tokens(code, state):
    if state == qiitainfo.STATE:
        url = 'https://qiita.com/api/v2/access_tokens'
        datas = {
            'client_id': qiitainfo.ID,
            'client_secret': qiitainfo.SECRET,
            'code': code,
        }
        return post(url, dumps(datas), headers=headers,)
    return Response()


def authenticated_user(token):
    url = 'https://qiita.com/api/v2/authenticated_user'
    headers['Authorization'] = 'Bearer ' + token
    # print('headers: %s' % headers)
    return get(url, headers=headers,)


def stocks(user_id, page=1, token=''):
    url = 'https://qiita.com/api/v2/users/' + user_id + '/stocks'
    headers['Authorization'] = 'Bearer ' + token
    params = {
        'page': page,
        'per_page': 20,
    }
    return get(url, params=params, headers=headers,)


if __name__ == '__main__':
    print('OAuth URL: %s' % authorize())
