import collections


od1 = collections.OrderedDict({
    'banana': 1,
    'apple': 2,
    'orange': 3,
    'pear': 4
})

od2 = collections.OrderedDict({
    'apple': 2,
    'banana': 1,
    'orange': 3,
    'pear': 4
})

# 通常のDictは中身の比較だけだが
# OrderedDictの場合は、中身の順番も比較対象となる
print(od1 == od2)

# 要素は一番後ろに追加される
od1['c'] = 100
print(od1)

# key名を元に昇順にソート
od3 = collections.OrderedDict(
    sorted(od1.items(), key=lambda x: x[0]))

print(od3)
