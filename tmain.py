from mailParser import mailParser as mp

def main():
    rawMime = ''
    with open('cook.mime.txt', 'rb') as xfile:
        rawMime = xfile.read()
        
    print(rawMime)
    msg = mp(rawMime)
    print('\n\n')
    print('From: ' + str(msg.getSender()))
    print('To: ' + str(msg.getRecipient()))
    #print('Subject: ' + str(msg.getSubject()))
    print('Message: ' + str(msg.getBody()))


main()
