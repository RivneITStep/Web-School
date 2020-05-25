from django.db import models
from datetime import datetime


class Blog(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    moderated = models.BooleanField(default=False)
    text_area = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    views = models.IntegerField()

    def __str__(self):
        return self.title


class Blog_Img(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    photo_main = models.ImageField(upload_to='blog_img/', blank=True)

    def __str__(self):
        return self.blog_id.title
