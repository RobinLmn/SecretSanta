import smtplib
import participants
import json

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = "example@gmail.com"
password = "password"
subject = "subject"
server = "smtp.gmail.com"

def get_contacts(filename):
    f = open(filename, 'r')
    dict = json.load(f)
    f.close()
    out = []

    for p in dict["participants"]:
        out.append(participants.Participant(p["name"], p["email"], p["forbidden_matches"]))
    return out

def read_template(filename):
    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    participants_list = get_contacts("participants.json")
    message_template = read_template("email_template.txt")

    s = smtplib.SMTP(server, port=587)
    s.starttls()
    s.login(email, password)
 
    participants.match(participants_list)

    for p in participants_list:
        msg = MIMEMultipart()
        
        message = message_template.substitute(PERSON_NAME=p.name.title(), PERSON_ASSIGNEE=p.assignee.name)

        msg['From']= email
        msg['To'] = p.email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg
        
    s.quit()
    
if __name__ == '__main__':
    main()