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
            # messages.success(request, "You are logged in")
            logged_in = True
            return redirect('pages:index')
        else:
            # messages.error(request, "Login or password incorrect")
            return redirect('accounts:sign_in')
    else:
        return render(request,'accounts/sign_in.html')


def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        stuff = request.POST['stuff']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(email=email).exists():
            return redirect('accounts:registration')
        else:
            user = User.objects.create_user(username = email, email=email, password=password, first_name=first_name, last_name=last_name,)
            user.save()
            if stuff == 'Я викладач':
                pass 
            elif stuff == 'Я студент':
                pass
            return redirect('accounts:sign_in')



    else:
        return render(request, "accounts/registration.html")        


def dashboard(request):
    return render(request,'accounts/dashboard.html')


def sign_out(request):
    auth.logout(request)
    # messages.success(request, "See you later!")
    return redirect("pages:index")