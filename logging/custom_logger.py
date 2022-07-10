import logging

#Create a custom logger
logger = logging.getLogger(__name__)

#Create handlers and set the levels
f_handler = logging.FileHandler('Test.log', mode='w')
f_handler.setLevel(logging.ERROR)

#Create formatters and add it to the handlers
f_format = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
f_handler.setFormatter(f_format)

# Add the handler to the logger object
logger.addHandler(f_handler)

#Print log output
logger.error("This is an error")