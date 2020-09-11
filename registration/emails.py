from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from registration.tokens import account_token


def send_mail(request):
    if request.method == 'POST' and 'send_mail' in request.POST:
        user = request.user
        if user.is_authenticated:
            token = account_token.make_token(user)
            uidb = urlsafe_base64_encode(force_bytes(user.pk))
        context = {
            'token1': token,
            'token2': token,
            'uidb': uidb
        }
        message = render_to_string('registration/magic.html', context)
        mail_subject = 'Magic link for login'
        email_send = EmailMessage(mail_subject, message, to=[user.email])
        email_send.content_subtype = "html"
        email_send.send()
        print('Magic link has been sent to your email!')