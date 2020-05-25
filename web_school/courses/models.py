from django.db import models
from accounts.models import Teacher

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    avelable = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    avelable = models.BooleanField(default=True)
    description = models.CharField(max_length=200)
    text_area = models.TextField(blank=True)
    file = models.FileField(upload_to='video_course', null=True, verbose_name="")
    

    def __str__(self):
        return self.title


class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    avelable = models.BooleanField(default=True)
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True)


    def __str__(self):
        return self.title