from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestModel(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='password', email='admin@localhost')
        author = User.objects.get(id=1)
        cate = Category.objects.create(name='AI', description='description')
        Post.objects.create(title='First', content='Content', author=author, summary = 'summary', category=cate)

    def test_get_absolute_url(self):
        f = Post.objects.get(id=1)
        self.assertEqual(f.get_absolute_url(), '/detail/1/')


class TestTemplates(TestCase):
    def test_user_notautenticated_redirect(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        




