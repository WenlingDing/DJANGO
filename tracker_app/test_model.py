from django.test import TestCase
from .models import Issue, User, Status, Issuetype, Pay

class UserTest(TestCase):
    
    def testCanCreateUser(self):
        userName = User(name="Alex")
        userName.save()
        
        user_name_from_db = User.objects.all().get(pk=userName.id)
        self.assertEqual(user_name_from_db.name, "Alex")
        self.assertEqual(user_name_from_db.id, userName.id)




        