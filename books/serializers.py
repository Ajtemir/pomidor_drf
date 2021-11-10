from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from books.models import Book, UserBookRelation

User = get_user_model()

class BookReaderSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class BooksSerializer(ModelSerializer):
    # likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    owner_name = serializers.CharField(source='owner.username', default="",
                                       read_only=True)
    readers = BookReaderSerializer(many=True, read_only=True)

    # source=reader

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'author_name',
                  # 'likes_count',
                  'annotated_likes',
                  'rating',
                  'owner_name',
                  'readers'
                  )

    # def get_likes_count(self, instance):
    #     return UserBookRelation.objects.filter(
    #         book=instance, like=True).count()


class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
