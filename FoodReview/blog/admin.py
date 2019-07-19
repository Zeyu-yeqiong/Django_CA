from django.contrib import admin
from blog.models import UserInfo

# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'age']


admin.site.register(UserInfo, BlogsPostAdmin)