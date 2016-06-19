import os, sys, csv, datetime

class logger:
    def logError(self, title, message):
        self._writeLogToFile(self._getTimestamp(), title, message, 'error')

    def logEvent(self, title, message):
        self._writeLogToFile(self._getTimestamp(), title, message, 'event')

    def _writeLogToFile(self, timestamp, title, message, logType):
        logFile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'log.txt')
        with open(logFile, 'ab') as file:
            writer = csv.writer(file)
            data = [timestamp, title, message, logType]
            writer.writerow(data)

    def _getTimestamp(self):
        return datetime.datetime.now().isoformat()

