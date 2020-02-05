import functools


# 引数をキー、関数の実行結果をバリューに持つdictでキャッシュを実現する
def memoize(f):
    memo = {}

    def _wrapper(n):
        if n not in memo:
            memo[n] = f(n)

        return memo[n]
    return _wrapper


@memoize
def long_func(n):
    r = 0
    for i in range(1000000):
        r += n * i
    return r


# memoizeと同じ機能を提供
# recently usedで5つまでキャッシュする
@functools.lru_cache(maxsize=5)
def long_func(n):
    r = 0
    for i in range(1000000):
        r += n * i
    return r


for i in range(10):
    print(long_func(i))

# キャッシュの情報を出力
print(long_func.cache_info())
# キャッシュのクリアを実行
long_func.cache_clear()


print('next run')
for i in range(10):
    print(long_func(i))
