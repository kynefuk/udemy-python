import contextlib
import sys


# for line in sys.stdin:
#    print(line)

# sys.stdout.write('hoge')

# sys.stderr.write('error')

# 出力(stdout)をリダイレクトする
with open('stdout.log', 'w') as f:
    with contextlib.redirect_stdout(f):
        print('hoge')
