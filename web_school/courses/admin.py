from django.contrib import admin

from .models import Course, Lesson, Task

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('course',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Task, TaskAdmin)
