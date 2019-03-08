from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User

class QuestionTest(TestCase):

    def test_question(self):

        response = self.client.get('/api/questions/')
        self.assertEqual(response.status_code, 200)
