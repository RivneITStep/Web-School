from django import forms
from .models import *

# class TeacherForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Teacher
#         fields = ('user', 'first_name', 'last_name', 'phone', 'email', 'photo_main', 'courses', 'body', 'facebook', 'twitter', 'linkedIn','google','password')



# class TeacherForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Student
#         fields = ('user', 'first_name', 'last_name', 'phone', 'email', 'photo_main', 'courses', 'body', 'facebook', 'twitter', 'linkedIn','google','password')




class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()