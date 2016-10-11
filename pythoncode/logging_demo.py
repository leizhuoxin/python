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

_rhandler=logging.handlers.RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=5)
_rhandler.setLevel(logging.INFO)
_rhandler.setFormatter(formatter2)
#_rhandler.set_name()

_fhandler=logging.FileHandler('log.txt','a','utf-8',False)
_fhandler.setLevel(logging.DEBUG)
_fhandler.setFormatter(formatter3)
#-----------------------------logging-----------------------
#logger1=logging.getLogger('logger1')
#logger1.addHandler(_streamHandler)
#logger1.addHandler(_rhandler)
##logger1.addFilter()


#root=logging.getLogger()
#root.addHandler(_rhandler)

logger1=logging.getLogger('logger1')
logger1.setLevel(logging.DEBUG)
logger1.addHandler(_streamHandler)
logger1.addHandler(_fhandler)






#-----------------------------fromatter-----------------------
#-----------------------------fromatter-----------------------
#-----------------------------fromatter-----------------------
#-----------------------------fromatter-----------------------
#-----------------------------config--------------------------
'''
#logger.conf
###############################################
[loggers]
keys=root,example01,example02
[logger_root]
level=DEBUG
handlers=hand01,hand02
[logger_example01]
handlers=hand01,hand02
qualname=example01
propagate=0
[logger_example02]
handlers=hand01,hand03
qualname=example02
propagate=0
###############################################
[handlers]
keys=hand01,hand02,hand03
[handler_hand01]
class=StreamHandler
level=INFO
formatter=form02
args=(sys.stderr,)
[handler_hand02]
class=FileHandler
level=DEBUG
formatter=form01
args=('myapp.log', 'a')
[handler_hand03]
class=handlers.RotatingFileHandler
level=INFO
formatter=form02
args=('myapp.log', 'a', 10*1024*1024, 5)
###############################################
[formatters]
keys=form01,form02
[formatter_form01]
format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s
datefmt=%a, %d %b %Y %H:%M:%S
[formatter_form02]
format=%(name)-12s: %(levelname)-8s %(message)s
datefmt=

#--------------------------call---------------
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

'''
