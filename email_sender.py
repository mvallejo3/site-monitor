
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class Email_Sender:
    sg = None
    message = None
    from_email = "info@photon.software"
    to_email = "mvallejo3@gmail.com"
    subject = ''
    content = ''

    def __init__(self) -> None:
        self.sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    def build_subject(self, domain: str, status: str):
        if status == 'on':
            self.subject = domain + ' is back online!'
        else:
            self.subject = domain + ' is down.'

    def build_content(self, domain: str, status: str):
        msg = ' is currently down.' if status == 'off' else ' appears to be back online.'
        self.content  = '<div>'
        self.content += '<h1>' + domain + msg + '</h1>'
        self.content += '<a href="//'+domain+'">'
        self.content += 'Take a look.'
        self.content += '</a>'
        self.content += '</div>'

    def build_message(self, domain: str, status: str):
        self.build_subject(domain, status)
        self.build_content(domain, status)
        self.message = Mail(
            from_email=self.from_email,
            to_emails=self.to_email,
            subject=self.subject,
            html_content=self.content
        )

    def try_send(self, domain: str, status: str):
        try:
            self.build_message(domain, status)
            print(self.subject)
            print(self.content)
            self.sg.send(self.message)
        except Exception as e:
            print(str(e))

if (__name__ == '__main__'):
    sender = Email_Sender()
    sender.build_message('cms.you.suck')
    sender.try_send()