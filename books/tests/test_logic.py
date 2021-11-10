from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from books.logic import operations, set_rating
from books.models import Book, UserBookRelation


class LogicTestCase(TestCase):

    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(6, 13, '-')
        self.assertEqual(-7, result)

    def test_multiply(self):
        result = operations(6, 13, '*')
        self.assertEqual(78, result)


class SetRatingTestCase(APITestCase):
    def setUp(self) -> None:
        user1 = User.objects.create(username='user_001', first_name='Ivan', last_name='Petrov')
        user2 = User.objects.create(username='user_002', first_name='Ivan', last_name='Sidorov')
        user3 = User.objects.create(username='user_003', first_name='1', last_name='2')
        self.book1 = Book.objects.create(name='test_book_1', price=25, author_name='author1',
                                         owner=user1)
        # book2 = Book.objects.create(name='test_book_2', price=251, author_name='author2')
        UserBookRelation.objects.create(user=user1, book=self.book1, like=True, rate=5)
        UserBookRelation.objects.create(user=user2, book=self.book1, like=True, rate=5)
        UserBookRelation.objects.create(user=user3, book=self.book1, like=True, rate=4)

        # UserBookRelation.objects.create(user=user1, book=book2, like=True, rate=4)
        # UserBookRelation.objects.create(user=user2, book=book2, like=True, rate=3)
        # UserBookRelation.objects.create(user=user3, book=book2, like=False)

    def test_ok(self):
        set_rating(self.book1)
        self.book1.refresh_from_db()
        self.assertEqual('4.67', str(self.book1.rating))
