import json
from django.test import TestCase
from gamepage import views

# Rock = 0
# Paper = 1
# Scissors = 2

# Winner = 0 == no winner
# Winner = 1 == User
# Winner = 2 == Opponent

class ResultViewTestCases(TestCase):
    def setUp(self) -> None:
        super().__init__()
        self.url = "/result/"

    def test_user_rock_opponent_rock(self):
        body = json.dumps({'user_choice': 0, 'opponent_choice': 0})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 0)

    def test_user_rock_opponent_paper(self):
        body = json.dumps({'user_choice': 0, 'opponent_choice': 1})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 2)

    def test_user_rock_opponent_scissors(self):
        body = json.dumps({'user_choice': 0, 'opponent_choice': 2})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 1)

    def test_user_paper_opponent_paper(self):
        body = json.dumps({'user_choice': 1, 'opponent_choice': 1})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 0)

    def test_user_paper_opponent_scissors(self):
        body = json.dumps({'user_choice': 1, 'opponent_choice': 2})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 2)

    def test_user_paper_opponent_rock(self):
        body = json.dumps({'user_choice': 1, 'opponent_choice': 0})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 1)

    def test_user_scissors_opponent_scissors(self):
        body = json.dumps({'user_choice': 2, 'opponent_choice': 2})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 0)

    def test_user_scissors_opponent_rock(self):
        body = json.dumps({'user_choice': 2, 'opponent_choice': 0})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 2)

    def test_user_scissors_opponent_paper(self):
        body = json.dumps({'user_choice': 2, 'opponent_choice': 1})

        result = self.client.post(self.url, body, content_type='application/json')
        winner = json.loads(result.content).get("winner")
        self.assertEqual(winner, 1)
