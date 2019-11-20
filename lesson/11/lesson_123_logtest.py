import logging

logger = logging.getLogger(__name__)

# ロガーに出力ファイルを設定する
handler = logging.FileHandler('logtest.log')
logger.addHandler(handler)


def do_something():
    logger.info('from log test')
