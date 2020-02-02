import contextlib


@contextlib.contextmanager
def tag(name):
    print(f'<{name}>')
    # yieldの所でデコレートする関数が実行される
    yield
    print(f'</{name}>')


@tag('h2')
def f(content):
    print(content)


# これでも同様の処理となる
with tag('h2'):
    print('hoge')
