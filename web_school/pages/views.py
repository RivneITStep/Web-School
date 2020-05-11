from django.shortcuts import render, redirect

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