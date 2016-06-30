# smsMail
Mass texting via email

## Introduction
This program was build out of a need to be able to text a large group of people without paying for a service to do that.  smsMail uses the capability of mobile phones to send a text message to an email address.  The addresses are stored in a database, then an approved "sender" can send messages to all the users by texting the same email address.

## Installation
### Requirements
* Linux (tested on CentOS 6.7)
* Python (tested with 2.6.6, but any should be fine)
* mailX (tested with 12.4)
* sqlite3
* A mail server that can pipe an email to a script (tested with standard cPanel that comes on most web hosts)

### Setting smsMail up with cPanel
1. Clone this repo on your server.  I reccommend not storing it in a public folder.
2. Give the main.py file write permissions. 'chmod +x main.py'
3. In the cpanel gui, navigate to Email > Forwarders > Add Forwarder.
4. Enter the address that you want to use for sending and receiving mail.
5. Click 'Advanced Options.'
6. Enter the location of the main.py file where you stored it earlier.  This path is relative to your home directory.
7. Open the main.py file for editing via your method of choice
8. Change the "sender" variable on line 4 to reflect the forwarder you created earlier.

## Other instructions
### Subscribing to messages
Users are added when they text the email address with any of a list of keywords.  Currently, the only keyword is "subscribe," but you can change this list in the main.py file.  The varable is "subscribeKeywords."

### Unsubscribing to messages
Users are removed when they text the email address with any of a list of keywords.  Currently, the only keywords are "unsubscribe" and "stop," but you can change this list in the main.py file.  The varable is "unsubscribeKeywords."

### Adding a sender
1. Have the person subscribe to messages.
2. Open the database, smsmail.db, in sqlite via the terminal. '$ sqlite3 smsmail.db'
3. Make sure the person has been subscribed. 'sqlite> .headers on' 'sqlite> .mode column' 'sqlite> SELECT * FROM User;'
4. Verify that the user's phone number email address is listed under address.  Should be something like 1234567890@mms.att.net.
5. Update the value of "isSender" to 1. 'sqlite> UPDATE User SET isSender=1 WHERE address="the-phone-number-email-address"'
6. Add the senders first and last names to the database. 'sqlite> UPDATE User SET FirstName="the-sender's-first-name" WHERE address="the-phone-number-email-address"' 'sqlite> UPDATE User SET LastName="the-sender's-last-name" WHERE address="the-phone-number-email-address"'
