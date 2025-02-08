from os import path
from zipfile import  ZipFile
from datetime import datetime
import shutil
#function to get current date and time
def get_time_date(): 
    #creating instance of current date and time
    now = datetime.now()
    #return the current date and time

    return(now.strftime("%d-%m-%Y_%H-%M_%S"))

def zip_logs():
    #Paths of the Log files
    log_dir = "logs/"
    #file ame for the zip file
    zip_name = "support_bundle_"  + get_time_date() 
    #iterating through the log files
    # for log_file in log_files: 
    #     if path.exists(log_file): #check if the logfile exists or not
    #         with ZipFile(zip_name, "a") as newzip: #opening the zip file in append mode
    #             #write the logfile to the zip file
    #             newzip.write(log_file)  
    shutil.make_archive(path.join("support bundle", zip_name), 'zip', log_dir)
    # return the zip file name