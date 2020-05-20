from django.contrib import admin

from .models import Course, Lesson

class CourseAdmin(admin.ModelAdmin):
    display=('id')

class LessonAdmin(admin.ModelAdmin):
    display = ('id')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
