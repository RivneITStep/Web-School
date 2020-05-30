from django.db import models
from accounts.models import Teacher, Student

class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    avelable = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='courses_img/', blank=True)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    avelable = models.BooleanField(default=True)
    ready_for_check = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    question = models.CharField(max_length=200)
    answer = models.TextField(blank=True)
    

    def __str__(self):
        return self.title