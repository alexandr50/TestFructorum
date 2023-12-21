from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class CustomUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = CustomUser.objects.create(
            email='testing@mail.com',
            password='123qwe'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        data = {
            'email': 'testemail@mail.ru',
            'password': '123qwe'
        }

        response = self.client.post(
            '/users/register/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(CustomUser.objects.all().first().email, 'testing@mail.com')

    def test_list_users(self):
        data = {
            'email': 'testemail@mail2.ru',
            'password': '123qwe'
        }
        CustomUser.objects.create(**data)
        response = self.client.get(
            '/users/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(CustomUser.objects.all().count(), 2)
        self.assertEqual(CustomUser.objects.all().first().email, 'testing@mail.com')
