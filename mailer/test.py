from localMailer import LocalMailer

m = LocalMailer("-tw", "thwbama@gmail.com")
m.construct(["2567100172@vzwpix.com", "bcc@tshows.us"], "This is a test message")
m.send()
