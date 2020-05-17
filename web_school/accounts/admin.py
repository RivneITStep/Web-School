from django.contrib import admin

from .models import Teacher, Student

class TeacherAdmin(admin.ModelAdmin):
    display=('id')

class StudentAdmin(admin.ModelAdmin):
    display = ('id')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
