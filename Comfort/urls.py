"""
URL configuration for Comfort project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from asosiy.views import MahsulotApiView, CreateAdminUserAPIView, Qarzdorlik_sotuvchiApiView, Qarzdorlik_mijozApiView, KirimApiView, MahsulotOzgartirishApiView,Qarzdorlik_sotuvchiOzgartirishApiView, Qarzdorlik_mijozOzgartirishApiView, KirimOzgartirishApiView, AdminLoginAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahsulot/', MahsulotApiView.as_view()),
    path('qarzdorlik_sotuvchi/', Qarzdorlik_sotuvchiApiView.as_view()),
    path('qarzdorlik_mijoz/', Qarzdorlik_mijozApiView.as_view()),
    path('kirim/', KirimApiView.as_view()),
    path('login/', AdminLoginAPIView.as_view()),
    path('adminuser/', CreateAdminUserAPIView.as_view()),

    path('mahsulot/<int:pk>/', MahsulotOzgartirishApiView.as_view()),
    path('qarzdorlik_s/<int:pk>/', Qarzdorlik_sotuvchiOzgartirishApiView.as_view()),
    path('qarzdorlik_m/<int:pk>/', Qarzdorlik_mijozOzgartirishApiView.as_view()),
    path('kirim/<int:pk>/', KirimOzgartirishApiView.as_view()),
    path('token/', obtain_auth_token, name='token_obtain'),  # Bu qatorda "name" atributi ham ko'rsatilishi kerak
]


