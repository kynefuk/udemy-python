import functools


def deco(f):
    # wrapsを使うことで、fの情報を取得できる
    @functools.wraps(f)
    def _wrapper():
        """Wrapper Docstring"""
        print('decorator')
        return f()
    return _wrapper


@deco
def sample():
    """Sample Docstring"""
    print('sample')


# @functools.wrapsを使うことで
# _wrapper()ではなく、sample()のDocstringを表示できる
print(sample.__doc__)