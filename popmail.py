# POP email client that will read emails from a POP server

# Start POP server:
# sudo service popa3d start

import poplib
from email.message import EmailMessage

server = "127.0.0.1"
user = "isildur"
passwd = "yourpassword"

# create POP object and store it to server
server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

# retrieve the number of emails(messages)
msgNum = len(server.list()[1])

# loop through the server to retrieve each of the messages and print them
for n in range(msgNum):
    for m in server.retr(n+1)[1]:
        print(m.decode())