"""
backend/scoreboard/test_views.py

Tests for the scorebord. We use the test client. Read more at
    https://docs.djangoproject.com/en/2.1/topics/testing/tools/
"""
import json
from django.test import TestCase, Client
from backend.scoreboard.models import KattisHandle

class ScoreboardPageViewTests(TestCase):
    """About page view tests for URLs:
    - /scoreboard/subscribe
    """
    def test_subscribe(self):
        """
        Tests the /scoreboard/subscribe enpoint
        """
        c = Client()
        user = KattisHandle(handle="Test")
        user.save()
        
        response = c.post('scoreboard/subscribe', 
            {"username": "Test"}
        )
        self.assertEqual(response.status_code, 200)
        query_set = KattisHandle.objects.filter(
            username = "Test"
        )
        self.assertEqual(query_set[0].subscribed)
