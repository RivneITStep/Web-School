from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
        path('edit_t_photo/', views.edit_t_photo, name="edit_t_photo"),
        path('edit_s_photo/', views.edit_s_photo, name="edit_s_photo"),
        path('wrong/<int:task_id>/', views.wrong, name="wrong"),
        path('success/<int:task_id>/', views.success, name="success"),

]