import csv
import collections


with open('230_names.csv', 'w') as csv_file:
    # CSVの列名
    fieldnames = ['first', 'last', 'address']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # 列名を書き込み
    writer.writeheader()

    writer.writerow({'first': 'Mike', 'last': 'Jacson', 'address': 'A'})
    writer.writerow({'first': 'Scott', 'last': 'Nike', 'address': 'B'})
    writer.writerow({'first': 'Jano', 'last': 'Stefan', 'address': 'C'})


with open('230_names.csv', 'r') as f:
    reader = csv.reader(f)
    print(next(reader))
    while reader:
        print(next(reader))

    # 1回目のnext(reader)でヘッダーを取り、Namesのプロパティとして指定
    Names = collections.namedtuple('Names', next(reader))

    for row in reader:
        names = Names(row[0], row[1], row[2])
        print(names.first, names.last, names.address)


""" Point = collections.namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
print(p1.x)

# tupleなので書き換えは不可
# p1.x = 50

# pの要素を一部置き換え新しいオブジェクトを生成
p2 = p._replace(x=500)

# _make()は引数にiterableを取る
p3 = Point._make([100, 200]) """
