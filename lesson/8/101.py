import tempfile


# 一時ファイルなので使い終わったら勝手に消してくれる
# w+で書き込み/読み込み
with tempfile.TemporaryFile(mode='w+') as t:
    print(t.name)
    t.write('hello')
    t.seek(0)
    print(t.read())


# 一時ファイルを保存する場合
with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test')
        f.seek(0)
        print(f.read())


# 一時ディレクトリを保存しないで使う場合
with tempfile.TemporaryDirectory() as td:
    print(td)


# 一時ディレクトリを作成保存する
temp_dir = tempfile.mkdtemp()
print(temp_dir)
