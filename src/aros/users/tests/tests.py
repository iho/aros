from django.test import TestCase
from users.tests.factories import UserFactory                                                                                                                                                                                                                           
from django.test import Client


class UsersCase(TestCase):
    def setUp(self):
        UserFactory.create_batch(10)
        # self.client 

    def test_users_displayed(self):
        response = self.client.get("/users/")
        self.assertContains(response, "user0")