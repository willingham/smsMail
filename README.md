# smsMail
Mass texting via email

## Introduction
This program was build out of a need to be able to text a large group of people without paying for a service to do that.

## Installation
### Requirements
* Linux (tested on CentOS 6.7)
* Python (tested with 2.6.6, but any should be fine)
* mailX (tested with 12.4)
* A mail server that can pipe an email to a script (tested with standard cPanel that comes on most web hosts)

### Setting smsMail up with cPanel
1. Clone this repo on your server.  I reccommend not storing it in a public folder.
2. Give the main.py file write permissions.

> chmod +x main.py

3. In the cpanel gui, navigate to Email > Forwarders > Add Forwarder.
3.1 Enter the address that you want to use for sending and receiving mail.
3.2 Click 'Advanced Options.'
3.3 Enter the location of the main.py file where you stored it earlier.  This path is relative to your home directory.

4. Open the main.py file for editing via your method of choice
4.1 Change the "sender" variable on line 4 to reflect the forwarder you created earlier.

All of the user data is stored in an sqlite database file, smsmail.db.  To add the first user, text the email address you created earlier with the word "subscribe."
