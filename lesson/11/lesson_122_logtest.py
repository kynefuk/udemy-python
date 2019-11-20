import logging

# loggerはlesson-122.pyのloggingの設定が受け継がれる
# 各ファイルごとにloggerを作り、ログレベル等を設定する必要がある
# __name__でファイル名をロガー名として設定
logger = logging.getLogger(__name__)


def do_something():
    logger.info('from log test')
