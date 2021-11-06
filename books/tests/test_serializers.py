from unittest import TestCase

from books.models import Book
from books.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book1 = Book.objects.create(name='test_book_1', price=25)
        book2 = Book.objects.create(name='test_book_2', price=251)
        data = BooksSerializer([book1, book2], many=True).data
        expected = [
            {
                'id': book1.id,
                'name': 'test_book_1',
                'price': '25.00'
            },
            {
                'id': book2.id,
                'name': 'test_book_2',
                'price': '251.00'
            },
        ]
        self.assertEqual(expected, data)
