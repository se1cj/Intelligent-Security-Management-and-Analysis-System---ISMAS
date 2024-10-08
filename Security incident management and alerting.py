import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'admin@yourdomain.com'
    msg['To'] = 'security@yourdomain.com'

    with smtplib.SMTP('smtp.yourdomain.com') as server:
        server.login('username', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
