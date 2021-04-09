import pwntools
import logging, coloredlogs
import os

def Remote():

def Local():
    

# Create formatters 
DETAILED = logging.Formatter("%(asctime)-30s %(module)-15s %(levelname)-8s %(funcName)-20s %(message)s")

# Custom Logger
logger = logging.getLogger(name)
coloredlogs.install(logger=logger,level=logging.DEBUG)
FileHandler = logging.FileHandler("DaemonBot_Errors.log")
FileHandler.setFormatter(DETAILED)
logger.addHandler(FileHandler)

try:
    Mode = input("Would you like to overflow a local or remote program").lower()
    if Mode not in ["remote","local"]:
        print("Mode Failure")
        exit(0)
except Error as e:
    logger.error(f"'{e}' was detected.")
    
if Mode == "remote"
    Remote()
elif Mode == "local"
    Local()