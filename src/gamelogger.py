import logging

'''Initialize logger'''
def init():
    logFormat = '%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s'
    logging.basicConfig(filename='_testgame.log', level=logging.DEBUG, format=logFormat)
    
    logFormatter = logging.Formatter(logFormat)
    rootLogger = logging.getLogger()

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    logging.info('#############################################')
    logging.info('#          Logger is initialized            #')
    logging.info('#############################################')
