import logging, smtplib
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import GenerateSupportBundle 


file ="D:/Dev/HPE/week-five/LogAnalyser/logapp/logs/msg/Maillog.txt"

# Object creation
loggerm = logging.getLogger()

# Setting the threshold of the logger to debug 
loggerm.setLevel(logging.DEBUG)

#Usin rotating file handler to capture logs inside a file
handlerm = logging.handlers.RotatingFileHandler(file, maxBytes=50000, backupCount=2)

# Sets format of record in log file
formatter = logging.Formatter('%(asctime)s - %(pathname)s - line: %(lineno)d - %(levelname)s - %(message)s', '%d-%m-%Y %H:%M:%S')
handlerm.setFormatter(formatter)

# Adds the specified handler to logger "MyLogger"
loggerm.addHandler(handlerm)

        
def mail():
    #From address
    MY_ADDRESS = "interns.hpe.2021@gmail.com"
    #create Smtp client session object
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    #put the SMTP connection in TLS(Transport layer security)
    s.starttls()
    loggerm.info("Logging in with address and password for sending the email\n")
    #login with email address and password
    s.login(MY_ADDRESS,"internsHpe2021")
        
    #get the names and emails ids from contact.txt
    names, emails = ['Sherin'],['18cs131@kpriet.ac.in']
    #get message template from message.txt
    message_template = Template('''Dear ${PERSON_NAME},\nWe are having a problem with out file concatenation application.
                                \nKindly look into the log files that has been attached.\n\nRegards''')

    for name, email in zip(names, emails):
        #create instance of mutipart MIME(Multipurpose Intenet Mail Extention)
        msg = MIMEMultipart()
        #Replacing with person name in message
        message  =  message_template.substitute({'PERSON_NAME':name})
        loggerm.info("Adding From address, To address and subject to the mail\n")
        #add From address
        msg['From'] = MY_ADDRESS
        #add To address
        msg['To']=email
        #add Subject
        msg['Subject'] = "Alert!! Something went Wrong"
        #attach the message to the MIME instance
        msg.attach(MIMEText(message, "plain"))
        #zip the log files and get the name of the file
        file_path, file_name = GenerateSupportBundle.zip_logs()
        loggerm.info("Receiving the Support Bundle zip file\n")
        #open the log file in read binary mode
        file = open(file_path, 'rb')
        #Creating MIMEBase instance
        part = MIMEBase('application', "octet-stream")
        #set file to the payload
        part.set_payload(file.read())
        #encode the the payload(file)
        encoders.encode_base64(part)
        #add the header to the file
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(file_name))
        #attach the file to the MIME instance
        msg.attach(part)
        #send the mail
        s.send_message(msg)
        loggerm.info("Mailing the support bundle zip file\n")
        #delete the message
        del msg
