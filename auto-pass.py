# what's the elvish word for friend?

import os, subprocess, smtplib
from base64 import b64encode

username = "localuser"
set_passwd = b64encode(os.urandom(64)).decode('utf-8') # Mellon

from_a = '<FromEmail>'
to_a = '<ToEmail>'
msg = """
Your new password is: {0}

Keep it secret, keep it safe.
"""

def change_passwd(user, passwd):
    chpasswd = subprocess.Popen(['chpasswd'],
                            stdin=subprocess.PIPE)

    chpasswd.communicate("{0}:{1}".format(user, passwd))

def send_mail(from_a, to_a, msg):
    username = "<<FromEmail>>"
    password = "<YourPassword>"
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login(username, password)
    server.sendmail(from_a, to_a, msg.format(set_passwd))
    server.quit()

if __name__ == ("__main__"):
    change_passwd(username, set_passwd)
    send_mail(from_a, to_a, msg)
