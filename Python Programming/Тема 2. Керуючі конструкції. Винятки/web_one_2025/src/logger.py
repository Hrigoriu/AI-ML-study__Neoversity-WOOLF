import logging


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)

            console_handler = logging.StreamHandler()
            file_handler = logging.FileHandler("out.log")

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

            cls._instance = logger
            cls._instance.info("Logger is configured")
        else:
            cls._instance.info(
                "Logger is already configured, no need to create a new logger"
            )
        return cls._instance


if __name__ == "__main__":
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)

    # console_handler = logging.StreamHandler()
    # file_handler = logging.FileHandler("out.log")

    # logger.addHandler(console_handler)
    # logger.addHandler(file_handler)

    # logger.info("Logger is configured")

    logger = Logger()
    logger_two = Logger()
    print(logger is logger_two)
