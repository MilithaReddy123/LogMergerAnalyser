import logging
import logging.handlers
from pathlib import Path
import datetime
from os import path
from string import Template
from zipfile import ZipFile
import logging
import logging.handlers
import shutil

# Object creation
logger = logging.getLogger()

# Setting the threshold of the logger to debug 
logger.setLevel(logging.DEBUG)

#Usin rotating file handler to capture logs inside a file

file ="D:/Dev/HPE/week-five/LogAnalyser/logapp/logs/msg/GenerateSPlog.txt"
handler = logging.handlers.RotatingFileHandler(file, maxBytes=50000, backupCount=2)

# Sets format of record in log file
formatter = logging.Formatter('%(asctime)s - %(pathname)s - line: %(lineno)d - %(levelname)s - %(message)s', '%d-%m-%Y %H:%M:%S')
handler.setFormatter(formatter)

# Adds the specified handler to logger "MyLogger"
logger.addHandler(handler)


def get_time_date(): 
    #creating instance of current date and time
    now = datetime.datetime.now()
    #return the current date and time
    return(now.strftime("%d-%m-%Y_%H-%M-%S"))

def zip_logs():
    #Paths of the Log files
    log_dir = "logs/"
    logger.info("Collecting log files from Support Bundle NT Service directory for zipping\n")

    #file ame for the zip file
    zip_name = "support_bundle_"  + get_time_date() 
    zip_path = path.join("support bundle", zip_name)
    #iterating through the log files
    logger.info("Writing log files from Support Bundle NT Service directory into zip file with append mode\n")
    shutil.make_archive(zip_path, 'zip', log_dir)
    
    # return the zip file name
    logger.info("Returning the zip file to the method email\n")
    return zip_path, zip_name
