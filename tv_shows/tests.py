from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import TvShow


class TvShowTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.tvshow = TvShow.objects.create(
            name="Hawkeye", rating=5, rater=self.user
        )

    def test_string_representation(self):
        self.assertEqual(str(self.tvshow), 'Hawkeye')

    def test_tvshow_content(self):
        self.assertEqual(self.tvshow.name, 'Hawkeye')
        self.assertEqual(self.tvshow.rating, 5)
        self.assertEqual(self.tvshow.rater.username, 'tester')
