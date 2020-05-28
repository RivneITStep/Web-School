from django.contrib import admin

from .models import Teacher, Student

class TeacherAdmin(admin.ModelAdmin):
    list_display=('id',"first_name")

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id',"first_name")

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
