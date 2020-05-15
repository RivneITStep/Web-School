from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    photo_main = models.ImageField(upload_to='teachers_photos/%Y/%m/%d', blank=True)
    course = models.CharField(max_length=200)


    def __str__(self):
        return self.last_name



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    free_access = models.BooleanField(default=False)
    paid_access = models.BooleanField(default=False)
    lesson_access = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='students_photos/%Y/%m/%d', blank=True)

    
    def __str__(self):
        return self.last_name