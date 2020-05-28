from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Course, Lesson, Task


def courses(request):
    if request.user.is_authenticated:
        course = Course.objects.all()
        lesson = Lesson.objects.all().filter()

        context = {
            'course':course,
            'lesson': lesson
        }
        
    return render(request, 'pages/available_courses.html',context)



def one_lesson(request,course_id):
    if request.user.is_authenticated:
        course = get_object_or_404(Course,id=course_id)
        lesson = Lesson.objects.all().filter(course = course)
        task = Task.objects.all()
        paginator = Paginator(lesson, 1)
        page = request.GET.get("page")
        paged_lesson = paginator.get_page(page)
        context = {
            'paged_lesson':paged_lesson,
            'lesson':lesson,
            'tasks':task,
        }
    return render(request, 'pages/one_lesson.html',context)

