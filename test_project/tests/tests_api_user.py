from django.contrib.auth import get_user_model
from django.test import  Client
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


User = get_user_model()


class ProfileTest(APITestCase):
    def setUp(self):
        self.auth_client = Client()
        self.user = User.objects.create_user(
            username="sarah",
            email="connor@skynet.com",
            password="terminator2000"
        )
        self.auth_client.force_login(self.user)


    def test_registration(self):
        """Создаем пользователя"""
        data = {"username": "test", "email": "test@skynet.com",
                "password": "terminator2000"}
        response = self.client.post("/api/v1/auth/users/", data)
        self.assertEqual(response.status_code, 201)


    def test_get_token(self):
        """Получение токена"""
        data = {"username": "sarah", "password": "terminator2000"}
        response = self.client.post("/api/v1/auth-token/token/login/", data)
        self.assertEqual(response.status_code, 200)


class ProfileTestGetPutDelete(APITestCase):
        def setUp(self):
            self.user = User.objects.create_user(username="davinci",
                                                 password="coolart1764",
                                                 email="connor@skynet.com")
            self.token = Token.objects.create(user=self.user)
            self.api_authentication()
            self.unauth_client = Client()


        def api_authentication(self):
            self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


        def test_get_all_users(self):
            """Получаем список всех зарегестрированных пользователей"""
            response = self.client.get("/api/v1/users/")
            self.assertEqual(response.status_code, 200)


        def test_get_user(self):
            """Получаем список всех зарегестрированных пользователей анонимом"""
            response = self.client.get("/api/v1/users/1/")
            self.assertEqual(response.status_code, 200)


        def test_get_user_unauth_client(self):
            """Получаем список всех зарегестрированных пользователей анонимом"""
            response = self.unauth_client.get("/api/v1/users/")
            self.assertEqual(response.status_code, 401)


        def test_user_put(self):
            """Иызменяем данне пользователя"""
            data = {"username": "Davinci","last_name": "Leo", "password": "terminator2000"}
            response = self.client.put("/api/v1/users/1/", data)
            self.assertEqual(response.status_code, 200)


        def test_user_put_unauth_client(self):
            """Изменяем данные пользователя анонимом"""
            data = {"username": "Davinci","last_name": "Leo", "password": "terminator2000"}
            response = self.unauth_client.put("/api/v1/users/1/", data)
            self.assertEqual(response.status_code, 401)

        def test_user_delete_client(self):
            """Удаляем данные пользователя"""
            response = self.client.delete("/api/v1/users/1/")
            self.assertEqual(response.status_code, 204)
