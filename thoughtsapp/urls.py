"""ourthoughts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.home,name="home" ),
    path('login',views.login_page,name="login" ),
    path('logout',views.logout_page,name="logout" ),
    path('register',views.register,name="register" ),
    path('user_details',views.user_details,name="user_details" ),
    path('save_user_Details/<int:id>',views.save_user_Details,name="save_user_Details" ),
    path('createpost',views.create_post,name="createpost"),
    path('addcatagory',views.add_catagory,name="addcatagory"),
    path('user_page',views.user_page,name="user_page"),
    path('delete_post/<int:id>',views.delete_post,name="delete_post"),
    path('update_post/<int:id>',views.update_post,name="update_post"),
    
]
