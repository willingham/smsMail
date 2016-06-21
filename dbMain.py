import dbInterface

db = dbInterface.dbInterface('smsmail.db')
db.addSubscriber('22222222')
db.addSender('1111111')
db.removeSubscriber('333')
db.removeSender('22222222')
print(db.isSender('1111asdf111'))
for i in db.getAllSubscribers():
    print(i[0])
db.close()
