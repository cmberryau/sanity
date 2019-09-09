from django.test import TestCase

from sanity.tasks import test_task


class TaskTests(TestCase):
    def test_test_task(self):
        test_task()
