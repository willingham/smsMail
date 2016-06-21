#! /usr/bin/python

from mailParser import mailParser
from dbInterface import dbInterface
from mailCreater import mailCreater
from logger import logger

import sys
from datetime import datetime


def main():
    sender = 'txt@t4c.tshows.us'
    subscribeText = 'You have been successfully subscribed.'
    unsubscribeText = 'You have been successfully subscribed'
    subscribeKeywords = ['subscribe']
    unsubscribeKeywords = ['unsubscribe', 'stop']
    db = dbInterface('smsmail.db')
    msg = mailParser(sys.stdin.read())

    if db.isSender(msg.getSender()):
        newMsg = mailCreater()
        newMsg.setSender(sender)
        newMsg.setBody(msg.getBody())
        
        recipients = ''
        for item in db.getAllSubscribers():
            recipients += item[0] + ','
        recipients = recipients[:-1]

        newMsg.setRecipients(recipients)
        newMsg.sendAllBcc()

    elif any(x in msg.getBody().lower() for x in subscribeKeywords()):
        db.addSubscriber(msg.getSender())
        newMsg = mailCreater()
        newMsg.setSender(sender)
        newMsg.setBody(welcomeText)
        newMsg.setRecipient(msg.getSender())
        newMsg.sendOne()
   
    elif any(x in msg.getBody().lower() for x in unsubscribeKeywords()):
        db.removeSubscriber(msg.getSender())
        newMsg.setSender(sender)
        newMsg.setBody(unsubscribeText)
        newMsg.setRecipient(msg.getSender())
        newmsg.sendOne()


main()
