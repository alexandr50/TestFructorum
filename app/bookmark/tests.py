from rest_framework import status
from rest_framework.test import APITestCase

from bookmark.models import Bookmark
from complation.models import Complation
from users.models import CustomUser


class BookmarksTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = CustomUser.objects.create(
            email='testing@mail.com',
            password='123qwe'
        )
        self.client.force_authenticate(user=self.user)
        self.complation = Complation.objects.create(
            title='testcomplation',
            short_description='test_description'
        )

    def test_create_bookmark(self):
        data = {
            'url': 'https://sky.pro/#giftpopup',
        }

        response = self.client.post(
            '/bookmarks/create/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(Bookmark.objects.all().count(), 1)
        self.assertEqual(Bookmark.objects.all().first().title, 'Skypro — Онлайн-университет от Skyeng')

    def test_delete_bookmark(self):
        data = {
            'title': 'test_title',
            'description': 'test_description',
            'url': 'https://sky.pro/#giftpopup',
            'type': 'website'
        }
        bookmark = Bookmark.objects.create(**data)
        response = self.client.delete(
            f'/bookmarks/delete/{bookmark.pk}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(Bookmark.objects.all().count(), 0)

    def test_add_to_complation(self):
        data = {
            'title': 'test_title',
            'description': 'test_description',
            'url': 'https://sky.pro/#giftpopup',
            'type': 'website'
        }
        bookmark = Bookmark.objects.create(**data)
        response = self.client.put(
            f'/bookmarks/update/{bookmark.pk}/',
            data={'complation': [{'id': 1}]},
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(Bookmark.objects.all().first().complation.all().first().title, 'testcomplation')
