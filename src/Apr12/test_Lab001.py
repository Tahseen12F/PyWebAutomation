# Logging
# It means capturing details which are useful while debugging.
# It presents users with the information of different types of logs -
"""Informational logs
Warning logs
Error logs
Critical logs"""

import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    # Intentional logging to user
    LOGGER.info("This is an informational log")
    LOGGER.warning("This is a warning log")
    LOGGER.error("This is an Error log")
    LOGGER.critical("This is a critical log")