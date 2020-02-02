import contextlib
import os


# ファイルが存在しない場合はpassする処理
try:
    os.remove('sample.txt')
except FileNotFoundError:
    pass


# suppressを使うと、エラーの発生を抑圧(無視)してくれる
with contextlib.suppress(FileNotFoundError):
    os.remove(('sample.txt'))