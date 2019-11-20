from collections import ChainMap


d1 = {'A': 'a', 'B': 'b', 'num': 0}
d2 = {'C': 'c', 'D': 'd'}


class DeepChainMap(ChainMap):
    """
    既存の値より大きい場合しか追加しない
    """

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                # valueがint かつ、既存の値よりvalueが大きい場合のみkeyの値を書き換える
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return

        # 合致するkeyがない場合は、一番初めのマップに追加する
        self.maps[0][key] = value


dcm = DeepChainMap(d1, d2)

# 既存のnumの値より大きいのでnumの値が1に書き換わる
dcm['num'] = 1


m = ChainMap(d1, d2)

d1['E'] = 'e'
d2['E'] = 'hoge'
# リスト形式でマップを保持
print(cm.maps)
# 重複したキーがある場合は、mapsのリストの手前にあるものが優先される
print(cm['E']) """
