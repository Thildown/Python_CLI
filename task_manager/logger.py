import logging
import os

def setup_logger(log_file="task_manager.log"):
    """Configure and setup logging for the application."""
    log_directory = "logs"
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    log_path = os.path.join(log_directory, log_file)
    
    # Setup logger
    logger = logging.getLogger("task_manager")
    logger.setLevel(logging.INFO)
    
    # If handlers are already configured, don't add more
    if not logger.handlers:
        # Create file handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        logger.info("Logger initialized")
    
    return logger