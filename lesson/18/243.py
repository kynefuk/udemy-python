import functools


def f(x, y):
    return x + y


def task(f):
    print('task start')
    print(f())

# 引数を必要とする関数を
# 別の関数の引数として実行する場合は
# クロージャを使う必要があるが、可読性が低い
""" def outer(x, y):
    def _inner():
        return x + y
    return _inner

g = outer(10, 20)
task(g) """

# partialで関数とその関数の引数を渡す書き方ができる
p = functools.partial(f, 10, 20)
task(p)
