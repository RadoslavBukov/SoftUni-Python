"""
Input	                                Output
Peter John Hi,John                      Peter says to John: Hi,John. Sent: True
John Peter Hi,Peter!                    John says to Peter: Hi,Peter!. Sent: False
Katy Lilly Hello,Lilly                  Katy says to Lilly: Hello,Lilly. Sent: True
Stop
0, 2

Anna, Bella, Hi                         Anna, says to Bella,: Hi. Sent: True
Sam, Dany, Okey                         Sam, says to Dany,: Okey. Sent: False
Felix, Mery, Bye                        Felix, says to Mery,: Bye. Sent: False
Stop
0
"""
class Email:
    def __init__(self,sender,reciever,content):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input().split(' ')

    if command[0] == "Stop":
        break

    sender = command[0]
    reciever = command[1]
    content = command[2]

    email = Email(sender, reciever, content)
    emails.append(email)

send_email = [emails[int(x)].send() for x in input().split(',  ')]

for email in emails:
    print(email.get_info())
