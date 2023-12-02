from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

router = SimpleRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = [
    path('detail/<int:pk>', PostDetail.as_view(), name="detail"),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),

] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)