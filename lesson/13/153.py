import urllib.request
import json


payload = {'key1': 'value1', 'key2': 'value2'}

# GETリクエスト
url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)

with urllib.request.urlopen(url) as f:
    # bytesで返ってきたデータをデコードしてJSONオブジェクトに変換
    print(json.loads(f.read().decode()))


# POSTリクエスト
# リクエストボディはbytesにする必要がある
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/post', data=payload, method='POST')

with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))