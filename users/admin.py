from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'bio', 'phone_no', 'facebook',)

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = 'Картинка'
# Register your models here.

admin.site.register(Profile, ProfileAdmin)