# Imports the Cloud Logging client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()

import logging
import sys

# get logger
logger = logging.getLogger()

# create formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
# cannot write to file in Google App Engine, read-only file system
# file_handler = logging.FileHandler('app.log')

# set formatters
stream_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# add handlers to the logger
logger.handlers = [stream_handler]

# set log level to INFO
logger.setLevel(logging.INFO)

