import smtplib
from mailer import Mailer


class LocalMailer(Mailer):
    def __init__(self, signature, sender):
        super(signature)
        self._sender = sender
        self._server = smtplib.SMTP('localhost')


    def construct(self, message):
        self._message = message

    def validate(self):
        return len(self._message) < 160

    def send(self):
        msg = MIMEMultipart('alternative')
        msg['BCC'] = ", ".join(self._recipients)
        body = MIMEText(self._message, 'plain')
        msg.attach(body)

        self._server.sendmail(self._sender, "thomas@tshows.us", msg.as_string())
