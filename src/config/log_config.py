
import logging
from logging import StreamHandler
from colorlog import ColoredFormatter
import logging
import sys

# Configure logging
logger = logging.getLogger("fastapi_logger")  # Create a logger
logger.setLevel(logging.DEBUG)  # Set the base logger level (captures all levels)

# Create a StreamHandler for logging to console
stream_handler = StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)  # Set log level for this handler

# Add function name and file path to the log format (each variable on a new line)
formatter = logging.Formatter(
    "\n%(asctime)s\n%(name)s\n%(levelname)s\n%(message)s\n[Function: %(funcName)s]\n[Path: %(pathname)s]\n",
    datefmt="%Y-%m-%d %H:%M:%S",
)
stream_handler.setFormatter(formatter)

# Add the StreamHandler to the logger
logger.addHandler(stream_handler)



# -----colored logs
# # Configure logging
# logger = logging.getLogger("fastapi_logger")
# logger.setLevel(logging.DEBUG)

# # Set up color formatter
# color_formatter = ColoredFormatter(
#     "\n%(asctime)s\n%(name)s\n%(levelname)s\n%(message)s\n[Function: %(funcName)s]\n[Path: %(pathname)s]\n",
#     datefmt="%Y-%m-%d %H:%M:%S",
#     log_colors={
#         "DEBUG": "cyan",
#         "INFO": "green",
#         "WARNING": "yellow",
#         "ERROR": "red",
#         "CRITICAL": "bold_red",
#     },
#     reset=True,  # Ensure ANSI reset codes are used
#     secondary_log_colors={},  # No additional colors for now
#     style="%",
# )

# # Create a console handler and attach the color formatter
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)
# console_handler.setFormatter(color_formatter)
# logger.addHandler(console_handler)