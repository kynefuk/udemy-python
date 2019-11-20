import logging

# levelnameはPythonが入れてくれる
# formatter = '%(levelname)s: %(message)s'

# asctimeでログが生成された時刻を出力
formatter = '%(asctime)s: %(message)s'

# https://docs.python.org/ja/3/library/logging.html

logging.basicConfig(level=logging.DEBUG, format=formatter)

logging.info('info %s: %s', 'test', 'test2')
