import subprocess

class mailCreater(object):
    def __init__(self):
        self._body = ''
        self._sender = ''
        self._recipient = ''
        self._recipients = ''

    def setBody(self, body):
        self._body = body

    def setSender(self, sender):
        self._sender = sender

    def setRecipient(self, recipient):
        self._recipient = recipient

    def setRecipients(self, recipients):
        self._recipients = recipients

    def sendOne(self):
        command = 'echo "%s" | mailx -r %s %s' % (self._body, self._sender, self._recipient)
        subprocess.call(command, shell=True)

    def sendAllBcc(self):
        command = 'echo "%s" | mailx -r %s -b %s %s' % (self._body, self._sender, self._recipients, self._sender)
        subprocess.call(command, shell=True)
