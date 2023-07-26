import os
import sys
import logging

# Define the logging format with timestamp, log level, module name, and log message.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create a directory for storing log files.
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings.
logging.basicConfig(
    level=logging.INFO,          # Set the logging level to INFO, which will log messages with level INFO and higher.
    format=logging_str,          # Use the defined logging format.
    handlers=[
        logging.FileHandler(log_filepath),    # Output logs to a file specified by log_filepath.
        logging.StreamHandler(sys.stdout)     # Output logs to the console (stdout).
    ]
)

# Create a logger instance for the "cnnClassifierLogger" namespace.
logger = logging.getLogger("cnnClassifierLogger")
