import collections


l = ['a', 'a', 'a', 'b', 'b', 'c']


d = dict()
for word in l:

    # wordが存在しなければvalueに0を入れる/ wordがあれば何もしない
    d.setdefault(word, 0)
    d[word] += 1

print(d)


# defaultdict()を使うと初期値を設定してくれるので、以下のような分岐を書かなくて済む
""" if key in d:
    # keyが入ってるときの処理
else:
    # keyが入っていないときの処理 """

# defaultdict()は引数に関数を受ける
# int()を引数として受けているので、初期値にint()の結果である「0」が入る
d = collections.defaultdict(int)

for word in l:
    d[word] += 1

print(d)

# set()を引数として受けるので、valueの初期値はSetになる
d = collections.defaultdict(set)
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

for key, value in s:
    d[key].add(value)

print(d)


d = collections.defaultdict(dict)

for key, value in s:
    d[key][key] = value

print(d)
