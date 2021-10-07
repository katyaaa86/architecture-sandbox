import smtplib
from email.mime.text import MIMEText


class Sender:
    def send(self, sender: str, recipient: str, message: str) -> None:
        msg = MIMEText(message)
        msg['From'] = sender
        msg['To'] = recipient

        mail_sender = smtplib.SMTP('localhost')
        mail_sender.send_message(msg)
        mail_sender.quit()


class Logger:
    def output(self, message: str) -> None:
        print(message)


if __name__ == '__main__':
    sender = Sender()
    sender.send(
        'me@example.com',
        'another@example.com',
        'This is your message',
    )
