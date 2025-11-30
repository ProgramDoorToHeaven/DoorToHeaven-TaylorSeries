# version 2025-07-27
from __future__ import annotations

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    # Configure logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Create a handler for stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# from logger_getter import get_logger
# LOGGER=get_logger(__name__)
