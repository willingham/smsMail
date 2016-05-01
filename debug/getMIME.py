#! /usr/bin/python

import sys

msg = sys.stdin.read()  # Read in raw email data
y = open("/home/tshows/scripts/t4c-email/mail-send-test.txt", "w", 1)
y.write(msg)
y.close()
