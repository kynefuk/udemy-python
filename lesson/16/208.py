import base64
import hashlib
import os

user_name = 'user1'
password = 'password'

db = {}

# テーブル表が漏洩しても大丈夫なようにpasswordにsaltを追加した値をハッシュ化する
salt = base64.b64encode(os.urandom(32))


def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(salt + password).hexdigest()

    ''' for _ in range(100):
        digest = hashlib.sha256((bytes(digest, 'utf-8')).hexdigest() '''

    return digest


def is_login(user_name, password):
    return get_digest(password) == db[user_name]


db[user_name] = get_digest(password)

print(is_login(user_name, password))
