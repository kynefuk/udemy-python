import collections
import queue


# First in First out のキュー
q = queue.Queue()

# Last in First out のキュー(最後にinしたものを最初にoutする)
lq = queue.LifoQueue()

# リスト
l = list()

# リストより高速なのでキューやスタックとしてデータを扱う際はdequeを使った方が良い
d = collections.deque()


for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

for _ in range(3):
    print('FIFO : {}'.format(q.get()))
    print('LIFO : {}'.format(lq.get()))
    print('LIST : {}'.format(l.pop(0)))
    print('DEQUE: {}'.format(d.popleft()))
