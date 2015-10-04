# what's the elvish word for friend?

import os, subprocess, smtplib, json
from base64 import b64encode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_user(): # Returns the currently logged in user.
    p = subprocess.check_output({'logname'})
    username = p.strip()
    if username != 'root': # Just in case...
        return username

def gen_passwd(n=12): # Returns a random password using /dev/urandom of n size (default 12 bytes)
    random_bytes = os.urandom(n)
    random_passwd = b64encode(random_bytes).decode('utf-8')
    return random_passwd

def change_passwd(user, passwd): # Pass user:passwd to chpasswd
    chpasswd = subprocess.Popen(['chpasswd'],
                            stdin=subprocess.PIPE)
    chpasswd.communicate("{USER}:{PASSWD}".format(USER=user, PASSWD=passwd))

def get_mail_cred(address_key='default-mail'): # Returns email credentials from email_cred.json
    with open('email_cred.json', 'r') as f:
        address_dict = json.load(f)
    return (address_dict[address_key][0], address_dict[address_key][1])

def gen_msg(user, passwd, FROM, TO): # Returns HTML email
    msg_content = """
    <p>Hi {USER}! Your new password is:<b> {PASSWD}</b></p>
    <p>Keep it secret, keep it safe!</p>""".format(USER=user, PASSWD=passwd)

    message = MIMEText(msg_content, 'html')
    message['From'] = 'Password Robot <{FROM}>'.format(FROM=FROM)
    message['To'] = '{USER} <{TO}>'.format(USER=user, TO=TO)
    message['Subject'] = 'New password for {USER}!'.format(USER=user)

    msg_full = message.as_string()
    return msg_full

def send_mail(mail_user, mail_pass, FROM, TO, MSG): # Send mail via smtplib / gmail
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(mail_user, mail_pass)
    server.sendmail(FROM, TO, MSG)
    server.quit()

if __name__ == ("__main__"):
    # Mellon
    username = get_user()
    random_passwd = gen_passwd()
    change_passwd(username, random_passwd)
    mail_user, mail_pass = get_mail_cred()

    FROM = mail_user
    TO = '<To@Adress.com>'
    MSG = gen_msg(username, random_passwd, FROM, TO)

    print("Connecting...")
    send_mail(mail_user, mail_pass, FROM, TO, MSG)
    print('Password sent to {user} <{email}>'.format(user=username, email=TO))
