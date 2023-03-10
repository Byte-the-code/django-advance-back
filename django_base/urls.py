from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


from django_base.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('users/', include('users.urls')),
    path('news/', include('news.urls')),
    path('coins/', include('coins.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
