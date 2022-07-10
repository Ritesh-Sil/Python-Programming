import logging

#2
# 2-a : level=logging.ERROR
# 2-b : filename="logging_python.txt"
# 2-c : filemode='w'
# 2-d : format='%(asctime)-%(name)s-%(levelname)s-%(message)s'

logging.basicConfig(level=logging.ERROR,
                    filename="logging_python.txt",
                    filemode='w',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

#1.
logging.debug("This is debug")
logging.info("This is info")
logging.warning("This is info")
logging.error("This is info")
logging.critical("This is info")
