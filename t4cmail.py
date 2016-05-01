#! /usr/bin/python

import sys, email, os, csv, traceback
from cStringIO import StringIO
from datetime import datetime


messageFooter = "\n\n**Text Stop at anytime to unsubscribe**"
recipientCSV = "/home/tshows/scripts/t4c-email/testrecords.csv"

def functions(messageContent, sender, to, subject):
    approvedSenders = ['2567100172@vzwpix.com','2564605075@mms.att.net', '2563184996@mms.att.net']
    if sender in approvedSenders and to == 'sendtext@t4c.tshows.us':
        send.message(messageContent)
    elif to == 'sendtext@t4c.tshows.us' and sender not in approvedSenders:
        addDeniedUser(sender)
        sys.exit()
    elif subject == 'Subscribe':
        addSubscriber(sender)
    elif sender == 'text@t4c.tshows.us':
        sys.exit()
    elif 'Subscribe' in messageContent:
        addSubscriber(sender)
    elif 'subscribe' in messageContent:
        addSubscriber(sender)
    elif 'Stop' in messageContent:
        removeSubscriber(sender)
    elif 'stop' in messageContent:
        removeSubscriber(sender)
    else:
        send.error(sender)

def getMessage():
    plain = False
    msg = sys.stdin.read()  # Read in raw email data
#     with open('/home/tshows/scripts/t4c-email/logs/sharp.txt', 'a') as file:
# 	    file.write(msg)
    origmsg = msg
    msg = email.message_from_string(msg)  # Parse MIME
    messageContent = ''  # Empty string to add message text to
    #  Add all message content to string
    if msg.is_multipart():
        for part in msg.get_payload():
            if part.get_content_type() == 'text/plain':
                messageContent += str(part.get_payload())
                plain = True
    else:
        messageContent += str(msg.get_payload())
    sender = email.utils.parseaddr(msg['from'])[1]  # Access the message sender
    to = email.utils.parseaddr(msg['to'])[1]  # Access the message sender
    subject = msg['subject']
    messageContent = messageContent.replace('\n', '')
    messageContent = messageContent.replace('\r', '')
    messageContent = messageContent.replace('=', '')
    return messageContent, sender, to, subject, origmsg

def addSubscriber(subscriber):
    with open(recipientCSV, 'rb') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == subscriber:
                send.alreadySubscribed(subscriber)
                sys.exit()
    file = open(recipientCSV, "a")
    mycsv = csv.writer(file)
    data = [[subscriber]]
    mycsv.writerow(data[0])
    file.close()
    send.subscribed(subscriber)

def addDeniedUser(sender):
    message = 'Nice try ;)'
    with open('/home/tshows/scripts/t4c-email/denied.csv', 'a') as file:
            mycsv = csv.writer(file)
            data = [[sender]]
            mycsv.writerow(data[0])
    send.send(sender,message)

def removeSubscriber(subscriber):
    removal_list = [subscriber]
    with open(recipientCSV, 'rb') as file_b:
        new_a_buf = StringIO()
        writer = csv.writer(new_a_buf)
        reader2 = csv.reader(file_b)
        next(reader2)
        for row in reader2:
            if row[0] not in removal_list:
                writer.writerow(row)

# At this point, the contents (new_a_buf) exist in memory
        with open(recipientCSV, 'wb') as file_a:
            file_a.write(new_a_buf.getvalue())
    send.removed(subscriber)

class sendMail:
    def error(self, recipient):
        subscrError = "Error: You have not sent a valid option.  Please try again."
        self.send(recipient, subscrError)

    def subscribed(self, recipient):
        subscr = "You have been successfully subscribed to T4C updates!"
        self.send(recipient, subscr)

    def alreadySubscribed(self, recipient):
        subscr = "You are already subscribed to T4C updates.  If you feel this may be an error, please send an email to thomas@tshows.us."
        self.send(recipient, subscr)

    def removed(self, recipient):
        removed = "You have been successfully removed and will no longer recieve T4C updates."
        self.send(recipient, removed)

    def message(self, message):
        message += messageFooter
        address = ''
        with open(recipientCSV) as csv_file:
            for row in csv.reader(csv_file):
                address += row[0] + ','
        self.sendBCC(address, message)

    def sendBCC(self, address, message):
        address = address[:-1]
        os.system('echo "' + message + '" | mailx -r text@t4c.tshows.us -b ' + address + ' text@t4c.tshows.us')

    def send(self, address, message):
        os.system('echo "' + message + '" | mailx -r text@t4c.tshows.us ' + address)

def main():
    try:
        message, sender, to, subject, origmsg = getMessage()
        functions(message, sender, to, subject)  # Figure out what to do with the sender
    except:
#         try:
        fname = '/home/tshows/scripts/t4c-email/logs/' + str(datetime.now()) + '.txt'
        sep = '#######################################################\n'
        with open(fname, 'w+') as file:
            file.write(traceback.format_exc())
            file.write(sep)
            file.write(sep)
            file.write(sep)
#             file.write(origmsg)
#             print(traceback.format_exc())
        sys.exit()
#         except:
#             sys.exit()

send = sendMail()

main()

########################################
#
#  Only for mass subscribing
#
########################################

# def subfunctions(sender):
#         addSubscriber(sender)
# 
# def subMain():
#     try:
#         message, sender, to, subject = getMessage()
#         subfunctions(sender)  # Figure out what to do with the sender
#     except:
#         sys.exit()
# 
# 
# subMain()

