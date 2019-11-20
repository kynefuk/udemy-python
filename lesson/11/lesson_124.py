import logging


logging.basicConfig(level=logging.INFO)


class NoPassFilter(logging.Filter):

    # ログに"password"の文字が含まれていない場合はログ出力する
    def filter(self, record):
        log_message = record.getMessage()

        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())

logger.info('from main')
logger.info('password: hogehoge')
