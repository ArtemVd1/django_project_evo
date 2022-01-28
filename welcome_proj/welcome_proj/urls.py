from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import welcome.views as views

urlpatterns = [
    path('welcome/', views.welcome_form, name='welcome_form'),
    path('welcome/list/', views.welcome_list, name='welcome_list'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
