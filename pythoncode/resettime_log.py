import logging
import logging.handlers

#-----------------------------fromatter-----------------------
formatter1=logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
formatter2=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
formatter3=logging.Formatter('%(message)s')

#-----------------------------hangler-------------------------
_streamHandler=logging.StreamHandler()
_streamHandler.setLevel(logging.DEBUG)
_streamHandler.setFormatter(formatter1)

_fhandler=logging.FileHandler('log.txt','a','utf-8',False)
_fhandler.setLevel(logging.DEBUG)
_fhandler.setFormatter(formatter3)
#-----------------------------logging-----------------------
logger1=logging.getLogger('logger1')
logger1.setLevel(logging.DEBUG)
logger1.addHandler(_streamHandler)
logger1.addHandler(_fhandler)