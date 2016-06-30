#! /usr/bin/python

from mailParser import mailParser
from dbInterface import dbInterface
from mailCreater import mailCreater
from logger import logger

import sys, traceback
from datetime import datetime


def main():
    sender = 'text@t4c.tshows.us'
    subscribeText = 'You have been successfully subscribed.'
    unsubscribeText = 'You have been successfully removed from updates.'
    subscribeKeywords = ['subscribe']
    unsubscribeKeywords = ['unsubscribe', 'stop']
    db = dbInterface('/home/tshows/scripts/t4c-email/smsmail.db')
    msg = mailParser(sys.stdin.read())
    if (msg.getSender() == sender):
        return

    elif db.isSender(msg.getSender()):
        newMsg = mailCreater()
        newMsg.setSender(sender)
        signature = '  -' + db.getFirstName(msg.getSender())[0] + '.' + db.getLastName(msg.getSender())
        newMsg.setBody(msg.getBody() + signature)
        
        recipients = ''
        for item in db.getAllSubscribers():
            recipients += item[0] + ','
        recipients = recipients[:-1]

        newMsg.setRecipients(recipients)
        newMsg.sendAllBcc()

    elif any(x in msg.getBody().lower() for x in unsubscribeKeywords):
        db.removeSubscriber(msg.getSender())
        newMsg = mailCreater()
	newMsg.setSender(sender)
        newMsg.setBody(unsubscribeText)
        newMsg.setRecipient(msg.getSender())
        newMsg.sendOne()

    elif any(x in msg.getBody().lower() for x in subscribeKeywords):
        db.addSubscriber(msg.getSender())
        newMsg = mailCreater()
        newMsg.setSender(sender)
        newMsg.setBody(subscribeText)
        newMsg.setRecipient(msg.getSender())
        newMsg.sendOne()
   
try:
    main()
    #sys.exit(1)
except:
    fname = "/home/tshows/scripts/t4c-email/logs/" + str(datetime.now()) + '.txt'
    sep = '##########################################################\n'
    with open(fname, 'w+') as file:
        file.write(traceback.format_exc())
        file.write(sep)
        file.write(sep)
        file.write(sep)
    #sys.exit(1)
