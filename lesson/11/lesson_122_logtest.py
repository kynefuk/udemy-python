import logging

# loggerはlesson-122.pyのloggingの設定が受け継がれる
# 各ファイルごとにloggerを作り、ログレベル等を設定する
# __name__でファイル名をロガー名として設定
# INFO: ファイル名: ログメッセージ という形式でログ出力される
logger = logging.getLogger(__name__)


def do_something():
    logger.info('from log test')
