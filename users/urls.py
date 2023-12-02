from django.urls import path

from .views import Register, Login, Logout, profile, profile_update, crete_profile, index

app_name='users'

urlpatterns = [
    path('welcome/', index, name='index'),
    path("register/", Register, name="register"),
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
    path('profile/<int:id>/', profile, name='profile'),
    path('create_profile/<int:id>/', crete_profile, name='create_profile'),
    path('profile_update/<int:id>/', profile_update, name='profile_update'),
]