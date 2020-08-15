import smtplib
from email import encoders
from email.mime.text import MIMEText  # for ordinary text
from email.mime.base import MIMEBase  # for attachments
from email.mime.multipart import MIMEMultipart  # to bring the entire email together

# start the smtp server
server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()

# load the password for file
with open('pass.txt', 'r') as f:
    password = f.read()

server.login('test@gmail.com', password)


# creating the email
msg = MIMEMultipart()
msg['From'] = "SpaceX Inc."
msg['To'] = "test@spaml.de"  # test email
msg['Subject'] = "Hello World!"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))  # add message to msg object

# creating attachment object
filename = 'attach.jpeg'
attachment = open(filename, 'rb')  # read-binary mode for images

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('content-disposition', f'attachment; filename={filename}')

msg.attach(p)  # add attachment to msg object

text = msg.as_string()
server.sendmail('test@gmail.com', 'test@spaml.de', text)
