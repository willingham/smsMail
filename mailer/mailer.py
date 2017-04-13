class Mailer:
    def __init__(self, signature=""):
        self._keys = {}
        self._message = ""
        self._recipients = []
        self._signature = signature

    def construct(self):
        pass

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
