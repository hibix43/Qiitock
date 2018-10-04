from socket import gethostname
from os import environ

ID = ''
SECRET = ''
STATE = ''
SESSION_SECRET_KEY = ''
HOSTNAME = gethostname()

if 'x1600' in HOSTNAME:
    import secret_ids
    ID = secret_ids.ID
    SECRET = secret_ids.SECRET
    STATE = secret_ids.STATE
    SESSION_SECRET_KEY = secret_ids.SESSION_SECRET_KEY
else:
    ID = environ['ID']
    SECRET = environ['SECRET']
    STATE = environ['STATE']
    SESSION_SECRET_KEY = environ['SESSION_SECRET_KEY']
