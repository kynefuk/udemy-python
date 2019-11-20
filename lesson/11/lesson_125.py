import logging.config

# 設定ファイルからロギングの設定
# logging.config.fileConfig('lesson_125_logging.ini')

# loggingの設定はDictConfigで行うことが多い
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'sampleFormatter': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'sampleHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'sampleFormatter',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['sampleHandlers'],
        'level': logging.WARNING
    },
    'loggers': {
        'simpleExample': {
            'handlers': ['sampleHandlers'],
            'level': logging.DEBUG,
            'propagate': 0
        }
    }
})

logger = logging.getLogger(__name__)

logger.debug('debug')
logger.info('info')
logger.warning('warninig')
logger.error('error')
logger.critical('critical')

""" logger = logging.getLogger('simpleExample')

logger.debug('debug')
logger.info('info')
logger.warning('warninig')
logger.error('error')
logger.critical('critical') """
