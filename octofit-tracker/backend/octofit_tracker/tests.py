from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Superman')
