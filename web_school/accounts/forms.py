from django import forms
from .models import *

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("photo_main",)



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("photo_main",)
