class mailParser(object):
    def __init__(self, rawMime):
        self._mime = email.message_from_string(rawMime)
        self._messageContent = ''

    def getSender(self):
        return email.utils.parseaddr(self._mime['from'])[1]

    def getRecipient(self):
        return email.utils.parseaddr(self._mime['to'])[1]
    
    def getSubject(self):
        return self._mime['subject']

    def getBody(self):
        if self._mime.is_multipart():
            for part in self._mime.get_payload():
                if part.get_filename() != '':
                    self._messageContent += part.get_payload(decode=True)
                if part.get_content_type() == 'text/plain':
                    self._messageContent += str(part.get_payload())
        else:
            if self._mime.get_filename() != '':
                self._messageContent += self._mime.get_payload(decode=True)
            else:
                self._messageContent += str(self._mime.get_payload())
        self._messageContent = self._messageContent\
                .replace('\n', '')\
                .replace('\r', '')\
                .replace('=', '')
        return self._messageContent
    
    def checkFor(self, s):
        continue

