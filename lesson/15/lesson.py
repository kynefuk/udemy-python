import logging
import multiprocessing


logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


def worker2(i):
    logging.debug('start')
    logging.debug(i)
    logging.debug('end')


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=worker1, args=(1,))
    t2 = multiprocessing.Process(name='renamed_process', target=worker2, args=(1,))
    t1.start()
    t2.start()
