import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from books.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create(username='test_username')
        self.book1 = Book.objects.create(name='test_book_1', price=25,
                                         author_name='author_1')
        self.book2 = Book.objects.create(name='test_book_2', price=55,
                                         author_name='author_2')
        self.book3 = Book.objects.create(name='test_book_3 author_1', price=55,
                                         author_name='author_1')


    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        # полный url необьязательно
        serializer_data = BooksSerializer([self.book1, self.book2, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK,
                         response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'author_1'})
        # полный url необьязательно
        serializer_data = BooksSerializer([self.book1, self.book3], many=True).data
        self.assertEqual(status.HTTP_200_OK,
                         response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        url = reverse('book-list')
        data = {
            "name": "Python 3",
            "price": 150,
            "author_name": "Mark Summerfield",
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data,
                                    content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
