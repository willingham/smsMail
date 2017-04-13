from mailer import Mailer
from bandwidth_sdk import Client, Message


class BandwidthMailer(Mailer):
    def __init__(self, signature="", providerInfo={}):
        super(BandwidthMailer, self).__init__(signature, providerInfo)
        Client(providerInfo["user"], providerInfo["token"], providerInfo["secret"])

    def construct(self, recipients, message):
        super(BandwidthMailer, self).construct(recipients, message)

    def validate(self):
        return len(self._message) < 160

    def send(self):
        for recipient in self._recipients:
            Message.send(
                    sender=self._providerInfo["sender"],
                    receiver=recipient,
                    text=self._message,
                    tag='test')
        return True

