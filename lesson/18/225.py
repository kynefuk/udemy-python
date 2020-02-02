import io
import requests
import zipfile


# インメモリーストリームで読み書きする
# StringIOは文字列BytesIOはバイナリ
f = io.StringIO()
f.write('宮尾')
# 書き込んだ後は行頭に戻って読み込む
f.seek(0)
print(f.read())


url = ('https://files.pythonhosted.org/packages/42/3e/'
       '2464120172859e5d103e5500315fb5555b1e908c0dacc73d80d35a9480ca/'
       'setuptools-45.1.0.zip')

f = io.BytesIO()

# zipファイルを取得
r = requests.get(url)
# インメモリに書き込み
f.write(r.content)

# zipファイルを開きREADMEを取得
with zipfile.ZipFile(f) as z:
    with z.open('setuptools-45.1.0/README.rst') as r:
        # バイナリをデコード
        print(r.read().decode())
