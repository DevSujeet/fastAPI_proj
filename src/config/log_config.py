
import logging
from colorlog import ColoredFormatter
import logging
import sys

# Configure logging
logger = logging.getLogger("fastapi_logger")
logger.setLevel(logging.DEBUG)

# Set up color formatter
color_formatter = ColoredFormatter(
    "\n%(asctime)s\n%(name)s\n%(levelname)s\n%(message)s\n[Function: %(funcName)s]\n[Path: %(pathname)s]\n",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
    reset=True,  # Ensure ANSI reset codes are used
    secondary_log_colors={},  # No additional colors for now
    style="%",
)

# Create a console handler and attach the color formatter
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(color_formatter)
logger.addHandler(console_handler)