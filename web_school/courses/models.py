from django.db import models

class Course(models.Model):
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