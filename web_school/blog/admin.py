from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('author','title','moderated','pub_date')


class Blog_ImgAdmin(admin.ModelAdmin):
    list_display = ('blog_id','photo_main')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Blog_Img, Blog_ImgAdmin)