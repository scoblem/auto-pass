# what's the elvish word for friend?

import os, subprocess, smtplib
from base64 import b64encode

from_a = '<FromEmail>'
to_a = '<ToEmail>'
msg = """
Your new password is: {0}

Keep it secret, keep it safe.
"""

def get_user():
    p = subprocess.check_output({'logname'})
    username = p.strip()
    if username != 'root': # just in case...
        return username

def gen_passwd(n=12):
    random_bytes = os.urandom(n)
    encoded_passwd = b64encode(random_bytes).decode('utf-8')

    return encoded_passwd

def change_passwd(user, passwd):
    chpasswd = subprocess.Popen(['chpasswd'],
                            stdin=subprocess.PIPE)

    chpasswd.communicate("{0}:{1}".format(user, passwd))

def gen_msg():
    pass

def send_mail(from_a, to_a, msg):
    username = "<FromEmail>"
    password = "<YourPassword>"
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(username, password)
    server.sendmail(from_a, to_a, msg.format(set_passwd))
    server.quit()

if __name__ == ("__main__"):
    # Mellon
    username = get_user()
    random_passwd = gen_passwd()

    change_passwd(username, random_passwd)
    # send_mail(from_a, to_a, msg)
    print(username)
    print(random_passwd)
