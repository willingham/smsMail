class Mailer:
    def __init__(self, signature="", keys={}):
        self._keys = keys
        self._message = ""
        self._recipients = []
        self._signature = signature

    def construct(self, recipients, message):
        self._recipients = recipients
        self._message = message

    def validate(self):
        pass

    def send(self):
        pass

    def getKeys(self):
        return self._keys

    def getMessage(self):
        return self._message

    def getRecipients(self):
        return self._recipients
