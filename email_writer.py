import smtplib
import ssl
from email.message import EmailMessage
import datetime

def send_strings_via_email(sender_email, app_password, recipient_email, doc_title, first_author, content):
    subject = f"The Crier: {datetime.date.today()}"
    dow = datetime.today().strftime('%A')
    greeting = f"Happy {dow} readers! Today we're diving into {doc_title} by firt author {first_author}"

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(greeting + "\n\n" + content)

    # Send email securely using Gmail SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print(f"Email sent successfully to {recipient_email}.")