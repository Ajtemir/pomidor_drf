from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from books.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book1 = Book.objects.create(name='test_book_1', price=25)
        book2 = Book.objects.create(name='test_book_2', price=251)
        url = reverse('book-list')
        response = self.client.get(url)
        # полный url необьязательно
        serializer_data = BooksSerializer([book1, book2], many=True).data
        self.assertEqual(status.HTTP_200_OK,
                         response.status_code)
        self.assertEqual(serializer_data, response.data)
