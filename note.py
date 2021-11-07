from rest_framework.routers import SimpleRouter

from books.views import BookViewSet

router = SimpleRouter()

router.register(r'book', BookViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls

# http://127.0.0.1:8000/book/?format=json

# test_logic.py must necessarily start with test

# ./manage.py test books.tests

# createuser -s -P superadmin
# creating super user postgresql
# psql --user=superadmin pomidorDRF_db
# ALTER USER pomidorDRF_user CREATEDB;
# ./manage.py test .
#all test
#response = self.client.get(url)
#response.data
# coverage run --source='.' ./manage.py test .
# coverage report
# coverage html
#json default
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

#
# after makemigrations with change model
# 1)add default
# 2) change default in model

permission_classes = [IsAuthenticated]
# network token session
# authentication there is there isnt
# authorization permissions

