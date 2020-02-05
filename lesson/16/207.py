import string
import random

from Crypto.Cipher import AES

# 暗号化する際にブロック単位で処理を行う(AES.block_size は16byte)
# 16文字の暗号化のキーが必要となる
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

# 初期ベクトル(同じ平文が同じ暗号文にならないようにするために使用するデータのこと)を生成
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)

with open('plaintext.txt', 'r') as f, open('enc.dat', 'wb') as e:
    plain_text = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 暗号化対象の文字列のサイズはブロックサイズの倍数でないといけないため
    # ブロックサイズになるように足りない文を足してあげる
    padding_length = AES.block_size - len(plain_text) % AES.block_size
    plain_text += chr(padding_length) * padding_length

    # 暗号化してファイルに書き込み
    cipher_text = cipher.encrypt(plain_text)
    e.write(cipher_text)

with open('enc.dat', 'rb') as e:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(e.read())

    print(decrypted_text)
    print(decrypted_text[-1])
    # 先頭からパディングで追加した文字列の前まで取得する
    print(decrypted_text[: -decrypted_text[-1]])