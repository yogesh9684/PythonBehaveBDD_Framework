import logging
def customLogger(Level=logging.DEBUG):

    # Get the name of the class / method from where this method is called
    logger = logging.getLogger()
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    #GetFileName
    fileHandler = logging.FileHandler("Moxie_Automation.log", mode='w')
    fileHandler.setLevel(Level)

    #GetFileFormatter

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s' , datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger