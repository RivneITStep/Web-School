from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
        path('available', views.courses, name="available_courses"),
        path('<int:course_id>/', views.one_lesson, name="one_lesson"),
        
]