import logging

FORMAT = '%(levelname)s %(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)

def main():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    print root_logger.level
    root_logger.info("info log")
    root_logger.warning("warning log")
    root_logger.error("error log")

if __name__=='__main__':
    main()