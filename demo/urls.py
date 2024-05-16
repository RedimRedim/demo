"""
URL configuration for demo project.

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
from django.urls import path, include
import debug_toolbar
from accounts import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")), #empty string which is home
    #path('main/', include("myapp.urls", namespace='main')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    #path('login/', LoginView.as_view(), name='login'),
    path('login/', views.login_request, name='login'),
]
