# For creating log files. 
import logging
import os
output_file_path = "media/output.txt"

def merge(source):
    # Configuring the log line 
    os.makedirs("logs/msg/", exist_ok=True)
    logging.basicConfig(filename='logs/msg/log_merger_log.txt', format='%(asctime)s -[%(pathname)s - %(lineno)d] - %(levelname)-8s %(message)s', filemode= 'a')

    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    # Creating a temporary file to store the merged content 
    logging.info("A temporary file to store the merged content is opened in write mode")
    temp_file = open('media/temp.txt','w')

    # opening the source file_1 in read mode
    logger.info("First target file is opened in read mode")
    target_file = open(output_file_path,'r')

    # Iterating over the src_file1 and writing the lines in the temporary file 
    logger.info("Iterating over each lines in the first source file and writing it to the temporary file")
    for lines in target_file:
        if(lines!='\n'):
            temp_file.write(lines)
    # Closing the first source file 
    logger.info("Closing the first source file stream")
    target_file.close()

    # Opening the source fiele_2 in read mode 
    logger.info("Second source file is opened in read mode")
    source_file = open(source,'r')
    # Iterating over the src_file2 and writing the lines in the targ_file
    logger.info("Iterating over each lines in the first source file and writing it to the temporary file")
    for lines in source_file:
     # Writing each line to the temp file 
        temp_file.write(lines)
    logger.info("Closing the second source file stream")
    source_file.close()
    # closing the temporary file as the writing operation is over 
    logger.info("Closing the temporary file stream")
    temp_file.close()

    # Opening the temporary file 
    logger.info("Opening the temporary file in read mode")
    temp_file = open('media/temp.txt','r')
    # Converting the entire file into an array, each line will become an element. 
    logger.info("Converting the entire file into an array, each line will become an element")
    lines_array = temp_file.readlines()
    # Sorting the array based on the date and time 
    logger.info("Sorting the array based on the date and time ")
    lines_array.sort()
    # Opening the target file 
    logger.info("Opening the target file")
    targ_file = open('media/output.txt','w')
    logger.info("Iterating over the array and writing it to the target file")
    for line in lines_array[::-1]:
        # Writing the sorted array elements to the target_file 
        if ord(line[0]) !=10:
            targ_file.write(line)
  
    logger.info("Closing the stream of the target file \n")
    targ_file.close()
