import smtplib
import csv
import participants

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Info:
    def __init__(self, filename):
        in_file = open(filename,'r', encoding = 'latin-1')
        self.email = in_file.readline().split("email: ", 1)[1]
        self.psswd = in_file.readline().split("password: ", 1)[1]
        self.forbiddenPairs = eval( (in_file.readline().split("forbidden pairs: ", 1)[1]) )
        self.subject = in_file.readline().split("subject: ", 1)[1]
        self.server = in_file.readline().split("server: ", 1)[1]

def get_contacts(filename):
    participants_list = []
    in_file = open(filename,'r', encoding = 'latin-1')

    line_to_process = in_file.readline()
    
    while len(line_to_process) != 0:
        
        elements = line_to_process.split(';')
        p = participants.Participant(elements[0], elements[2], elements[1])

        participants_list.append(p)
        line_to_process = in_file.readline()

    return participants_list

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    participants_list = get_contacts("participants_list.txt")
    message_template = read_template("email_template.txt")
    info = Info("info.txt")

    s = smtplib.SMTP(host=info.server, port=587)
    s.starttls()
    s.login(info.email, info.psswd)
 
    participants.match(participants_list, info.forbiddenPairs)

    for p in participants_list:
        msg = MIMEMultipart()
        
        message = message_template.substitute(PERSON_NAME=p.name.title(),\
                                              PERSON_ADDRESS=p.assignee.address.title(),\
                                              PERSON_ASSIGNEE=p.assignee.name)
                                
        msg['From']= info.email
        msg['To'] = p.email
        msg['Subject'] = info.subject
        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg
        
    s.quit()
    
if __name__ == '__main__':
    main()