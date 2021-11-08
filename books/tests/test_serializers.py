from unittest import TestCase

from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Avg

from books.models import Book, UserBookRelation
from books.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user_001')
        user2 = User.objects.create(username='user_002')
        user3 = User.objects.create(username='user_003')
        book1 = Book.objects.create(name='test_book_1', price=25, author_name='author1')
        book2 = Book.objects.create(name='test_book_2', price=251, author_name='author2')
        UserBookRelation.objects.create(user=user1, book=book1, like=True, rate=5)
        UserBookRelation.objects.create(user=user2, book=book1, like=True, rate=5)
        UserBookRelation.objects.create(user=user3, book=book1, like=True, rate=4)

        UserBookRelation.objects.create(user=user1, book=book2, like=True, rate=4)
        UserBookRelation.objects.create(user=user2, book=book2, like=True, rate=3)
        UserBookRelation.objects.create(user=user3, book=book2, like=False)
        books = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')).order_by('id')
        # data = BooksSerializer([book1, book2], many=True).data
        data = BooksSerializer(books, many=True).data
        expected = [
            {
                'id': book1.id,
                'name': 'test_book_1',
                'price': '25.00',
                'author_name': 'author1',
                'likes_count': 3,
                'annotated_likes': 3,
                'rating': '4.67'
            },
            {
                'id': book2.id,
                'name': 'test_book_2',
                'price': '251.00',
                'author_name': 'author2',
                'likes_count': 2,
                'annotated_likes': 2,
                'rating': '3.50'
            },
        ]
        print('=================')
        print(expected)
        print('=================')
        print(data)
        print('=================')

        self.assertEqual(expected, data)
