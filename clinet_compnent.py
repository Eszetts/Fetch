import jwt
import time
import requests


def send(data):
    state = "".join(data.split(":")[1:]).strip()
    encoded = encode(state)
    send_to_server(encoded)


def encode(state):
    payload = {
        "iss": "shuxiao.wang",
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "aud": "shuxiao.wang",
        "stat": state
    }
    return jwt.encode(payload, 'Jeyfhd556*$%', 'HS256')

def send_to_server(content):
    r = requests.post('http://ssapi.shuxiao.wang/addstate', data=content)
    if r.status_code != requests.codes.ok:
        print('{}-{}-{}'.format(r.status_code, content, int(time.time()))
