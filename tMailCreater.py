import mailCreater

msg = mailCreater.mailCreater()
msg.setBody('Hello, World')
msg.setSender('txt@t4c.tshows.us')
msg.setRecipient('thomas@tshows.us')
msg.sendOne()
