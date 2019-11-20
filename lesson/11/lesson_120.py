import logging

# デフォルトだと[warning]以上のログしか出ない
logging.basicConfig(filename='test.log', level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')

# logging特有の書き方
logging.info('info %s: %s', 'test', 'test2')

# 通常の書き方
logging.info('info %s: %s' % ('test', 'test2'))
logging.info('info {}: {}'.format('test', 'test2'))
