import requests


payload = {'key1': 'value1', 'key2': 'value2'}

# GETリクエスト
url = 'http://httpbin.org/get'

r = requests.get(url, params=payload)
print(r.status_code)
print(r.text)
print(r.json())


# POSTリクエスト
url = 'http://httpbin.org/post'

r = requests.post(url, data=payload)
print(r.status_code)
print(r.text)
print(r.json())
