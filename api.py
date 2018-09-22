import qiitainfo
from urllib import parse
from requests import get, post


def oauth_url():
    url = 'https://qiita.com/api/v2/oauth/authorize'
    params = {
        'client_id': qiitainfo.ID,
        'scope': 'read_qiita',
        'state': qiitainfo.STATE,
    }
    return url + '?' + parse.urlencode(params)
    # results = get(url, params=params)
    # return results

if __name__ == '__main__':
    print('OAuth URL: %s' % oauth_url())
    # print('OAuth Response Text: %s' % oauth_url().text)
