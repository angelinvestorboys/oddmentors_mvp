from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage


def send_mail(subject,template_name,context,recipients):
    ctx = context
    message = get_template(template_name).render(ctx)
    msg = EmailMessage(
        subject,
        message,
        "adebisiayomide68@gmail.com",
        recipients,
    )
    msg.content_subtype = "html"  # Main content is now text/html
    msg.send()
    print("Mail successfully sent")


def send_welcome_mail():
    pass

def send_create_event_email():
    pass

def send_event_reminder_email():
    pass

def send_create_mentorship_session_email():
    pass

def send_update_event_email():
    # send to all registered users
    pass

def send_decline_session_email():
    pass

def send_welcome_mail():
    pass

def send_welcome_mail():
    pass

