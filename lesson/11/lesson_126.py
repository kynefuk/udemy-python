import logging

logger = logging.getLogger(__name__)


# ファイル書き込みする処理
def save(self, csv_file):

    # ファイル書き込み処理の前にファイル名などをロギングする
    logger.info({
        'action': 'save',
        'csv': self.csv_file,
        'status': 'run'
    })

    # ファイル書き込み処理

    # ファイル書き込みが正常に終了したことをロギンスする
    logger.info({
        'action': 'save',
        'csv': self.csv_file,
        'status': 'success'
    })
