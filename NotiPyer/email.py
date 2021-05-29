import smtplib

def send_email(email_contents):
    """
    """
    from config import email_configs     
    gmail_user = email_configs['gmail_send_user']
    gmail_password = email_configs['gmail_send_password']

    sent_from = gmail_user
    to = email_configs['email_recipient']
    subject = str(email_contents['subject'])
    body = email_contents['body']

    email_text = """\
From: %s
To: %s
Subject: %s

%s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')