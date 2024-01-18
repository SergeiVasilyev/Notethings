"""
URL configuration for notethings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

from noteapp.views import main, new_note, logout_view, home, note, edit_note, create_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('new_note/', new_note, name='new_note'),
    path('create_note/', create_note, name='create_note'),
    path('logout/', logout_view, name='logout_view'),
    path('home/', home, name='home'),
    path('note/<int:idx>/', note, name='note'),
    path('edit_note/<int:idx>/', edit_note, name='edit_note'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
