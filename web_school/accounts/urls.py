from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
        path('sign_in/', views.sign_in, name="sign_in"),
        path('sign_out/', views.sign_out, name="sign_out"),
        path('registration/', views.registration, name="registration"),
        path('dashboard/', views.dashboard, name="dashboard"),
]