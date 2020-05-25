from django.shortcuts import render, redirect
from accounts.models import Student, Teacher
from django.shortcuts import get_object_or_404
from django.contrib import messages, auth
from courses.models import Course, Lesson


def index(request):
    teacher = Teacher.objects.all()
    return render(request, 'pages/index.html', context={'teachers':teacher})


def about(request):
    
    return render(request, 'pages/about.html')


def courses(request):
    
    return render(request, 'pages/courses.html')


def contacts(request):
    
    return render(request, 'pages/contacts.html')


def teachers(request):
    teacher = Teacher.objects.all()
    course = Course.objects.all()
    return render(request, 'pages/teachers.html',context={'teachers':teacher,'courses':course})



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
        profile = Teacher.objects.get(user=request.user.id)
        courses = Course.objects.all().filter(teacher=profile)
        context = {
            'profile': profile,
            'courses': courses
            }

    return render(request, 'pages/teacher_profile.html',context)

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