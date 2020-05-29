from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.core.paginator import Paginator
from .models import Course, Lesson, Task


def courses(request):
    if request.user.is_authenticated:
        course = Course.objects.all()
        lesson = Lesson.objects.all().filter()

        context = {
            'courses':course,
            'lessons': lesson
        }
        
    return render(request, 'pages/available_courses.html',context)



def one_lesson(request,course_id):
    if request.method == 'POST':
        student_answer = request.POST['student_answer']
        task_id = request.POST['task_id']
        ready_for_check = Task.objects.get(pk=task_id)
        ready_for_check.ready_for_check = True
        ready_for_check.answer = student_answer
        messages.success(request,'Your answer going for check!')
        ready_for_check.save()
        return redirect('pages:student_profile')

    if request.user.is_authenticated:
        course = get_object_or_404(Course,id=course_id)
        lesson = Lesson.objects.all().filter(course = course)
        task = Task.objects.all().filter(student=request.user.student)
        paginator = Paginator(lesson, 1)
        page = request.GET.get("page")
        paged_lesson = paginator.get_page(page)
        context = {
            'paged_lesson':paged_lesson,
            'lesson':lesson,
            'tasks':task,
        }
    return render(request, 'pages/one_lesson.html',context)

