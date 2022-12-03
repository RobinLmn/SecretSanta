import smtplib
import participants

from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Info:
    def __init__(self, filename):
        f = open(filename,'r', encoding = 'latin-1')
        self.email =    f.readline().split("email: ", 1)[1]
        self.psswd =    f.readline().split("password: ", 1)[1]
        self.subject =  f.readline().split("subject: ", 1)[1]
        self.server =   f.readline().split("server: ", 1)[1]

def get_contacts(filename):
    participants_list = []
    f = open(filename,'r')
    
    for line in f:
        args = line.split(';')
        p = participants.Participant(args[0], args[1], args[2::])
        participants_list.append(p)

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
 
    participants.match(participants_list)

    for p in participants_list:
        msg = MIMEMultipart()
        
        message = message_template.substitute(PERSON_NAME=p.name.title(),\
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