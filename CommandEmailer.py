from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import time
import os
import smtplib
# import Antenna_Tracker_and_RFD_Controls_GUI


class CommandEmailer():

    # Initialization of IMEI number
    def __init__(self, IMEI):
        # Pull from IMEI outlined in main window
        print "Function called"
        self.IMEI = IMEI
        print IMEI

    def sendCut(self):

        command = 'cutdown'
        self.send(command)
        print "Cutdown command sent"

        # print "Problem sending cutdown"

    def sendIdle(self):

        self.send('idle')
        print "Idle command sent"
    # Method used to send an email.

    def send(self, command):
        # Used to determine which file to send out

        if(command == 'cutdown'):
            fileOut = 'Command/cutdown.sbd'
        if(command == 'idle'):
            fileOut = 'Command/idle.sbd'

        # Builds and sends the email
        command = str(fileOut)
        print("Sendng: %s" % command)
        fromaddr = "msgc.borealis@gmail.com"
        toaddr = "data@sbd.iridium.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = self.IMEI
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(command, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename=%s' % command)
        body = ""
        msg.attach(MIMEText(body, "plain"))
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("msgc.borealis", "FlyHighN0w")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
