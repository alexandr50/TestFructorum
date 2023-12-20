from rest_framework import status
from rest_framework.test import APITestCase

from complation.models import Complation


class ComplationTestCase(APITestCase):

    def test_create_complation(self):
        data = {
            'title': 'test_title',
            'short_description': 'test_description'
        }

        response = self.client.post(
            '/complations/create/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(Complation.objects.all().count(), 1)
        self.assertEqual(Complation.objects.all().first().title, 'test_title')

    def test_list_complations(self):
        data = {
            'title': 'test_title',
            'short_description': 'test_description'
        }
        Complation.objects.create(**data)
        Complation.objects.create(**data)
        response = self.client.get(
            '/complations/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Complation.objects.all().count(), 2)
        self.assertEqual(Complation.objects.all().first().title, 'test_title')

    def test_update_complation(self):
        data = {
            'title': 'test_title',
            'short_description': 'test_description'
        }
        data_for_update = {
            'title': 'test_title_update',
            'short_description': 'test_description_update'
        }

        complation = Complation.objects.create(**data)
        response = self.client.put(
            f'/complations/update/{complation.pk}/',
            data=data_for_update,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Complation.objects.all().count(), 1)
        self.assertEqual(Complation.objects.all().first().title, 'test_title_update')

    def test_delete_complation(self):
        data = {
            'title': 'test_title',
            'short_description': 'test_description'
        }

        complation = Complation.objects.create(**data)
        response = self.client.delete(
            f'/complations/delete/{complation.pk}/',

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(Complation.objects.all().count(), 0)
        self.assertEqual(len(Complation.objects.all()), 0)
