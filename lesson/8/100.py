import glob
import zipfile


with zipfile.ZipFile('test.zip', 'w') as z:
    # zip化するデータを全て指定する
    # z.write('test_dir')
    # z.write('test_dir/test.txt')

    # **とrecursive=Trueでディレクトリ配下を全部やってくれる
    for f in glob.glob('test_dir/**', recursive=True):
        z.write(f)


with zipfile.ZipFile('test.zip', 'r') as z:
    # sampleというフォルダ名で展開する
    # z.extractall('sample')
    
    with z.open('test_dir/test.txt') as t:
        print(t.read().decode())