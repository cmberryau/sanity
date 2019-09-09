from django.apps import AppConfig
from django.core.mail import send_mail

from project.settings import HOST_NAME
from project.settings import ADMINS


class SanityConfig(AppConfig):
    name = 'sanity'

    # called on sanity app startup
    def ready(self):
        self.ensure_email()

    def ensure_email(self):
        send_mail(
            subject='Sanity app started',
            message='The sanity app has started - here is an email sent out as a test',
            from_email=f'sanity@{HOST_NAME}',
            recipient_list=[
                ADMINS[0]
            ],
            fail_silently=False,
        )
        print('Sent test email')
