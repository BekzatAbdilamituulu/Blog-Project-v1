from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Пользовател')
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True, verbose_name='Фото')
    bio = models.TextField(blank=True, null=True, verbose_name='Биография')
    phone_no = models.IntegerField(blank=True, null=True, verbose_name='Телефон')
    facebook = models.CharField(max_length=128, blank=True, null=True, verbose_name='Фейсбук')
   
    class Meta():
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'id': self.pk})
