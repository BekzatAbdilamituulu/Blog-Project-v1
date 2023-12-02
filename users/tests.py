from django.test import TestCase
from django import setup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
setup()
from users.models import Profile
from django.contrib.auth.models import User
from users.forms import ProfileForm
from django.urls import resolve
from users.views import index



class HomePageTest(TestCase):
    def test_root_url_resolve_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление домашней страницы'''
        found = resolve('/welcome/')
        self.assertEqual(found.func, index)
    
    def test_home_page_returns_correct_html(self):
        '''тест: html код главной страницы соответствует ожидаемому'''
        response = self.client.get('/welcome/')
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<h1>'))

    def test_uses_home_template(self):
        '''тест: шаблон home используется для рендеринга главной страницы'''
        response = self.client.get('/welcome/')
        self.assertTemplateUsed(response, 'users/base.html')
    
    def test_login_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'users/login.html')


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser(username='admin', password='password', email='admin@localhost')
        cls.user.profile = Profile.objects.create(user=cls.user, bio='bio', phone_no='22526', facebook='testfacebko')
    
    def test_bio_label(self):
        author = Profile.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'Биография')
    
        
    def test_absolute_url(self):
        author = Profile.objects.get(id=1)
        self.assertEqual(author.get_absolute_url(), '/profile/1/')

class ProfileFormTest(TestCase):

    def test_form_inputs(self):
        form = ProfileForm()
        expected = 4
        actual = len(list(form))
        self.assertEqual(expected, actual)

        