from django.test import Client, TestCase

from users.tests.factories import UserFactory


class UsersCase(TestCase):
    def test_users_displayed(self):
        UserFactory.create_batch(2)

        response = self.client.get("/users/")
        self.assertContains(response, "user")

    def test_user_create(self):
        self.client.post(
            "/users/new",
            {
                "username": "test_user",
                "password": "password",
                "email": "test@example.com",
            },
        )
        response = self.client.get("/users/")
        self.assertContains(response, "test_user")

    def test_user_update(self):
        user = UserFactory()
        self.client.post(
            f"/users/{user.id}",
            {
                "username": "test_user2",
                "password": "password",
                "email": "test@example.com",
            },
        )
        response = self.client.get("/users/")
        self.assertContains(response, "test_user2")
