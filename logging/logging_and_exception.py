import logging

try:
    print(name)

except Exception as e:
    #3
    logging.basicConfig(level=logging.DEBUG,
                    filename="logging_python.txt",
                    filemode='w',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    #4. exc_info=False means just write the log messege, if True , then start to Stack traces.
    logging.error("Error occured",exc_info=False)
