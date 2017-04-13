import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from mailer import Mailer


class LocalMailer(Mailer):
    def __init__(self, signature, sender):
        super(LocalMailer, self).__init__(signature)
        self._sender = sender
        self._server = smtplib.SMTP('localhost')

    def construct(self, recipients, message):
        super(LocalMailer, self).construct(recipients, message)

    def validate(self):
        return len(self._message) < 160

    def send(self):
        msg = MIMEText(self._message, 'plain')
        msg['From'] = self._sender
        msg['Bcc'] = ", ".join(self._recipients)
        try:
            self._server.send_message(msg))
            return True
        except:
            return False

    def quit(self):
        self._server.quit()
