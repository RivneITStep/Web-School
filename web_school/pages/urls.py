from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
        path('', views.index, name="index"),
        path('about/', views.about, name="about"),
        path('courses/', views.courses, name="courses"),
        path('contacts/', views.contacts, name="contacts"),
        path('teachers/', views.teachers, name="teachers"),
        path('testimonials/', views.testimonials, name="testimonials"),
        path('course_page/', views.course_page, name="course_page"),
        path('price/', views.price, name="price"),
        path('payment/', views.payment, name="payment"),
        path('teacher_profile/', views.teacher_profile, name="teacher_profile"),
        path('student_profile/', views.student_profile, name="student_profile"),
        path('student/', views.edit_student, name="edit_student"),
        path('teacher/', views.edit_teacher, name="edit_teacher"),
        path('edit_photo/', views.edit_photo, name="edit_photo"),
]