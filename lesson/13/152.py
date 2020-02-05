import json


j = {
    'employee': [
        {
            'id': 111,
            'name': 'Mike'
        },
        {
            'id': 222,
            'name': 'Nancy'
        }
    ]
}

# 辞書をJSON形式に整形した文字列にする
json_obj = json.dumps(j)
# JSONなので全てダブルクオーテーションになる
print(json_obj)

# JSON文字列を辞書に変換
dic = json.loads(json_obj)
print(dic)

# 辞書をJSONファイルとして保存
with open('test.json', 'w') as f:
    json.dump(j, f)


# JSONファイルを辞書として読み込む
with open('test.json', 'r') as f:
    print(json.load(f))
