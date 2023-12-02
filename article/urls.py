from django.urls import path
from .views import article_list_view, About, Contact, PostTemplateView, post_detail, category_detail, add_post, update_post, delete_post
app_name = 'article'

urlpatterns = [
    path('', article_list_view, name='home'),
    path('detail/<int:pk>/', post_detail, name='detail'),
    path('addpost/', add_post, name='add_post'),
    path('updatepost/<int:pk>/', update_post, name='update_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('post/', PostTemplateView.as_view(), name='post'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('category/<int:cat_id>/', category_detail, name='category'),
]
