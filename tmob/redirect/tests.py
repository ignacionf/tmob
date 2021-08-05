from django.test import TestCase
from redirect.models import Redirect

class RedirectTestCase(TestCase):
    def setUp(self):
        Redirect.objects.create(key="test1", url="http://localhost", active=True)

    def test_redirect_can_get(self):
        redirect = Redirect.objects.get_redirect("test1")
        self.assertEqual(redirect, {"key": "test1", "url": "http://localhost", "active": True})

