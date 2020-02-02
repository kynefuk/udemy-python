import tarfile


# モードで:gzを指定する必要がある
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    # addしたものが含まれた.gzが作成される
    tr.add('test_dir')


with tarfile.open('test.tar.gz', 'r:gz') as tar:
    # 指定したpathに展開する
    # tar.extractall(path='text_tar')

    # 指定したファイルをオープンする
    with tar.extractfile('test_dir/test.txt') as f:
        print(f.read().decode())