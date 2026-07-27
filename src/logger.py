"""
=========================================================
Project : 60 Days Real World Databricks Challenge
Module  : logger.py
Purpose : Centralized Logging Utility
=========================================================
"""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger.
    """

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
