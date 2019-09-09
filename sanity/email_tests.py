from django.test import TestCase
from django.core import mail
from django.core.mail import send_mail


class EmailTests(TestCase):
    # test emails will not actually use the backend
    def test_send_email(self):
        send_mail(
            subject='Subject here',
            message='Here is the message.',
            from_email='from@example.com',
            recipient_list=['to@example.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)
