from django.shortcuts import render, redirect
from accounts.models import Student, Teacher
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages, auth
from courses.models import Course, Lesson, Task
from blog.models import Blog, Blog_Img, Testimonials


def index(request):
    teacher = Teacher.objects.all()
    paginator = Paginator(teacher, 3)
    page = request.GET.get("page")
    teacher = paginator.get_page(page)
    blog_list = Blog.objects.filter(moderated=True).order_by('-pub_date')[:3]
    blog_img = Blog_Img.objects.all()
    courses = Course.objects.all()
    students = Student.objects.all()
    testimonial_list = Testimonials.objects.all().order_by('-pub_date')[:3]

    return render(request, 'pages/index.html', context={'teachers':teacher,'blog_list':blog_list,'imges':blog_img,'courses':courses,'students':students,'testimonials':testimonial_list})


def about(request):
    
    return render(request, 'pages/about.html')


def courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 2)
    page = request.GET.get("page")
    courses = paginator.get_page(page)
    return render(request, 'pages/courses.html',context={
        'courses':courses
    })


def contacts(request):
    
    return render(request, 'pages/contacts.html')


def teachers(request):
    teacher = Teacher.objects.all()
    course = Course.objects.all()
    return render(request, 'pages/teachers.html',context={'teachers':teacher,'courses':course})



def testimonials(request):
    if request.method == 'POST':
        text_area = request.POST['text_area']
        author_id = request.POST['author_id']
        teacher_id = request.POST['teacher_id']
        course_id = request.POST['course_id']
        student_id = request.POST['student_id']
        new_testimonial = Testimonials.objects.create(text_area=text_area,author_id=author_id,teacher_id=teacher_id,course_id=course_id,student_id=student_id)
        messages.success(request,'Your testimonial will be published after moderation!')
        new_testimonial.save()
        return redirect('pages:testimonials')
    courses = Course.objects.all().order_by("title")
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    testimonial_list = Testimonials.objects.all().order_by('-pub_date')
    paginator = Paginator(testimonial_list, 3)
    page = request.GET.get("page")
    testimonial_list = paginator.get_page(page)
    context={
        "teachers":teachers,
        "courses":courses,
        'testimonial_list':testimonial_list,
        'students': students
    }
    return render(request, 'pages/testimonials.html',context)



def course_page(request):
    
    return render(request, 'pages/course_page.html')



def price(request):
    
    return render(request, 'pages/price.html')


    
def payment(request):
    
    return render(request, 'pages/payment.html')


    
def teacher_profile(request):
    if request.user.is_authenticated:
        profile = Teacher.objects.get(user=request.user)
        courses = Course.objects.all().filter(teacher=profile)
        lessons = Lesson.objects.all().filter(course=courses)
        tasks = Task.objects.all().filter(ready_for_check = True)
        context = {
            'profile': profile,
            'courses': courses,
            'tasks':tasks,
            'lessons':lessons
            }

        return render(request, 'pages/teacher_profile.html',context)

    else:
        return render(request, 'pages/teacher_profile.html')



def student_profile(request):
    if request.user.is_authenticated:
        profile = Student.objects.get(user=request.user.id)
        context = {
            'profile': profile
        }
        return render(request, 'pages/student_profile.html',context)





def available_courses(request):
    
    return render(request, 'pages/available_courses.html')



def edit_student(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_email = request.POST['user_email']
        user_id = request.POST['user_id']
        course = request.POST['course']
        body = request.POST['body']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        linkedIn = request.POST['linkedIn']
        google = request.POST['google']
        profile = Student.objects.get(id=user_id)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.email = email
        profile.body = body
        profile.facebook = facebook
        profile.twitter = twitter
        profile.linkedIn = linkedIn
        profile.google = google
        request.user.email = email
        request.user.username = email
        request.user.save()
        profile.save()
        messages.success(request, "Your information was updated!")
    if request.user.is_authenticated:
        profile = Student.objects.get(user=request.user)
        context = {
            'profile': profile
        }
    return render(request, 'pages/edit.html',context)



def edit_teacher(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_email = request.POST['user_email']
        user_id = request.POST['user_id']
        course = request.POST['course']
        body = request.POST['body']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        linkedIn = request.POST['linkedIn']
        google = request.POST['google']
        profile = Teacher.objects.get(id=user_id)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.email = email
        profile.courses = course
        profile.body = body
        profile.facebook = facebook
        profile.twitter = twitter
        profile.linkedIn = linkedIn
        profile.google = google
        request.user.email = email
        request.user.username = email
        request.user.save()
        profile.save()
        messages.success(request, "Your information was updated!")

    if request.user.is_authenticated:
        profile = Teacher.objects.get(user=request.user)
        context = {
            'profile': profile
        }
    return render(request, 'pages/edit.html',context)



def edit_photo(request):
    # if request.method == "POST":
    #     img = request.POST['img']
    #     persona = request.POST['persona']
    #     student = get_object_or_404(Student, email=persona)
    #     if img:
    #         if student:
    #             student.photo_main = 'students_photos/' + img
    #             student.save()
    #         else:
    #             teacher = get_object_or_404(Teacher,email=persona)
    #             teacher.photo_main = 'teachers_photos/' + img
    #             teacher.save()
    #         return render(request, 'pages/edit.html')
    #     else:
    #         return render(request, 'pages/edit.html')
    return render(request, 'pages/edit.html')
    
    

def edit_profile(request):
    if request.method == "POST":
        pass



def wrong(request,task_id):
    wrong_task = Task.objects.get(id=task_id)
    wrong_task.ready_for_check = False
    wrong_task.save()
    return redirect('pages:teacher_profile')


def success(request,task_id):
    success_task = Task.objects.get(id=task_id)
    success_task.checked = True
    success_task.save()
    return redirect('pages:teacher_profile')