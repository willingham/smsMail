file = open("/home/tshows/scripts/t4c-email/records.csv", "rb")
csvArray = csv.reader(file)
file.close()
for address in csvArray:
    if address == subscriber:
        True = True
