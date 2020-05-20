from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Teacher, Student

def sign_in(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in")
            logged_in = True
            if user.is_staff == True:
                messages.success(request, "Wellcome Teacher")

                return redirect('pages:teacher_profile')
            else:
                messages.success(request, "Wellcome Student")

                return redirect('pages:student_profile')

        else:
            messages.error(request, "Login or password incorrect")
            return redirect('accounts:sign_in')
    else:
        return render(request,'accounts/sign_in.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        staff = request.POST['stuff']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(email=email).exists():
            messages.error(request, "This e-mail allready taken")
            return redirect('accounts:registration')
        if staff == 'Я викладач':
                staff = True
                user = User.objects.create_user(username = email, email=email,password=password,is_staff=staff, first_name=first_name, last_name=last_name)
                new_teacher = Teacher.objects.create(user=user, email=email, first_name=first_name, last_name=last_name)
                new_teacher.save()
                return redirect('accounts:sign_in')
        elif staff == 'Я студент':
                staff = False
                user = User.objects.create_user(username = email, email=email,password=password,is_staff=staff)
                new_student = Student.objects.create(user=user, email=email, first_name=first_name, last_name=last_name)
                new_student.save()
                return redirect('accounts:sign_in')
        else:
            return redirect('accounts:sign_in')



    else:
        return render(request, "accounts/registration.html")        


def dashboard(request):
    return render(request,'accounts/dashboard.html')


def sign_out(request):
    auth.logout(request)
    messages.success(request, "See you later!")
    return redirect("pages:index")