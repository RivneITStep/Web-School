from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
        path('', views.index, name="index"),
        path('about/', views.about, name="about"),
        path('courses/', views.courses, name="courses"),
        path('contacts/', views.contacts, name="contacts"),
        path('teachers/', views.teachers, name="teachers"),
        path('blog/', views.blog, name="blog"),
        path('testimonials/', views.testimonials, name="testimonials"),
        path('course_page/', views.course_page, name="course_page"),
        path('price/', views.price, name="price"),
        path('payment/', views.payment, name="payment"),
]