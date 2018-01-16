import logging

'''Initialize logger'''
def init():
    logging.basicConfig(filename='_testgame.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info('#############################################')
    logging.info('#          Logger is initialized            #')
    logging.info('#############################################')
