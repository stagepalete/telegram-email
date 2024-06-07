import logging
import os
from logging.handlers import RotatingFileHandler

# Define a function to configure logging
def configure_logging(log_file_path='app.log', log_level=logging.INFO):
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Create handlers
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    
    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    
    # Add handlers to the logger
    logger.addHandler(c_handler)