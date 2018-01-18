import sys
import logging

'''Initialize logger'''
def init(logFilename='_testgame.log'):
    logFormat = '%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s'
    logDir = "logs/"
    logging.basicConfig(filename=logDir+logFilename, level=logging.DEBUG, format=logFormat)

    logFormatter = logging.Formatter(logFormat)
    rootLogger = logging.getLogger()

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    logging.info('#############################################')
    logging.info('#          Logger is initialized            #')
    logging.info('#############################################')
