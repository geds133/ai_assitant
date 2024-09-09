import logging

# Set up the logger
def setup_logger():
    # Create a logger
    logger = logging.getLogger('memory_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    handler = logging.FileHandler('backend/logs/context_app.log')
    handler.setLevel(logging.DEBUG)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handlers to the logger
    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger

# Example usage of the logger
if __name__ == '__main__':
    logger = setup_logger()

