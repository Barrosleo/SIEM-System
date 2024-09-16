import smtplib
from email.mime.text import MIMEText

def send_email_alerts(alerts):
    msg = MIMEText("\n".join(alerts))
    msg['Subject'] = 'SIEM System Alerts'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.sendmail('your_email@example.com', ['recipient@example.com'], msg.as_string())
