from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', include('pages.urls')),
        path('account/', include('accounts.urls')),
        path('courses/', include('courses.urls')),
        path('blog/', include('blog.urls')),
        path('grappelli/', include('grappelli.urls')),
        path('admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
