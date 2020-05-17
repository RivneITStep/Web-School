from django.shortcuts import render, redirect
from accounts.models import Student, Teacher

def index(request):
    
    return render(request, 'pages/index.html')


def about(request):
    
    return render(request, 'pages/about.html')


def courses(request):
    
    return render(request, 'pages/courses.html')


def contacts(request):
    
    return render(request, 'pages/contacts.html')


def teachers(request):
    
    return render(request, 'pages/teachers.html')


def blog(request):
    
    return render(request, 'pages/blog.html')


def testimonials(request):
    
    return render(request, 'pages/testimonials.html')


def course_page(request):
    
    return render(request, 'pages/course_page.html')


def price(request):
    
    return render(request, 'pages/price.html')

    
def payment(request):
    
    return render(request, 'pages/payment.html')
    
def teacher_profile(request):
    if request.user.is_authenticated:
        profile = Teacher.objects.all().filter(email=request.user.username)
        context = {
            'profile': profile
            }

    return render(request, 'pages/teacher_profile.html',context)

def student_profile(request):
    if request.user.is_authenticated:
        profile = Student.objects.all().filter(email=request.user.username)
        context = {
            'profile': profile
        }
        return render(request, 'pages/student_profile.html',context)


def one_lesson(request):
    
    return render(request, 'pages/one_lesson.html')


def available_courses(request):
    
    return render(request, 'pages/available_courses.html')


def edit(request):
    
    return render(request, 'pages/edit.html')
