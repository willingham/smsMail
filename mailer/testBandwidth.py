from bandwidthMailer import BandwidthMailer

opts = {}
opts["user"] = "u-eya6c4sghkgfeods67fuzwq"
opts["token"] = "t-tuzkty2jb54tqvhydehy7nq"
opts["secret"] = "zxoizrel37vg6tr6ncynxvq4d62rjcrfrrihwia"
opts["sender"] = "+12056501468"

m = BandwidthMailer("-tw", opts)
m.construct(['+12567100172'], "test message")
m.send()
