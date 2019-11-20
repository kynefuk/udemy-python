import collections


l = ['a', 'a', 'a', 'b', 'b', 'c']

# Counterは辞書型dictのサブクラスで、キーに要素、値に出現回数という形のデータを持つ。
c = collections.Counter()

for value in l:
    c[value] += 1
print(c)
