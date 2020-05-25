from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    photo_main = models.ImageField(upload_to='teachers_photos/', blank=True)
    courses = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    linkedIn = models.CharField(max_length=500, blank=True)
    google = models.CharField(max_length=500, blank=True)



    def __str__(self):
        return 'Teacher {}'.format(self.user.username)



class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    free_access = models.BooleanField(default=False)
    paid_access = models.BooleanField(default=False)
    lesson_access = models.BooleanField(default=False)
    body = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='students_photos/', blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    linkedIn = models.CharField(max_length=500, blank=True)
    google = models.CharField(max_length=500, blank=True)

    
    def __str__(self):
        return 'Student {}'.format(self.user.username)