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