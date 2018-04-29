import logging
import time
from os import listdir
from os.path import basename
from subprocess import Popen
from sys import executable

start_time = time.time()

suffix = '.py'
if __name__ == '__main__':
    formatter = logging.Formatter('%(asctime)s : %(name)s :: %(levelname)s : %(message)s')
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    console_handler.setLevel(logging.DEBUG)
    logger.debug('started')

    base_file_name = basename(__file__)
    logger.debug('we are running from %s' % base_file_name)
    do_not_run = [base_file_name, '__init__.py']
    logger.debug('our do not run list is %s' % do_not_run)

    for script_file in listdir('.'):
        if script_file.endswith(suffix) and script_file not in do_not_run:
            logger.debug('we are running %s' % script_file)
            child = Popen([executable, script_file, '--username', 'root'])


    logger.debug('done')
    finish_time = time.time()
    elapsed_hours, elapsed_remainder = divmod(finish_time - start_time, 3600)
    elapsed_minutes, elapsed_seconds = divmod(elapsed_remainder, 60)
    logger.info('Time: {:0>2}:{:0>2}:{:05.2f}'.format(int(elapsed_hours), int(elapsed_minutes), elapsed_seconds))
    console_handler.close()
    logger.removeHandler(console_handler)
