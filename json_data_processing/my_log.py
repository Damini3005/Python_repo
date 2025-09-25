import logging

# Configure the logging system
logging.basicConfig(level=logging.INFO)

logging.debug("This message will NOT be shown, because the level is INFO.")
logging.info("This message WILL now be shown.")
logging.warning("This one will also be shown.")
logging.error("code it")
logging.critical("code it")

try:
  logging.info(9+"a")
except:
  logging.error("some thing wrong.")
