from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Category)
# Register your models here.
