"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from CookieTracker.view import account
from CookieTracker.view import other
from CookieTracker.view import forum

from CookieTracker import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('login/', account.login, name='login'),
    path('signup/', account.signup, name='signup'),
    path('logout/', account.logout, name='logout'),

    path('articles/', other.articles, name='articles'),
    path('exercises/', other.exercises, name='exercises'),
    path('debloat/', other.debloat, name='debloat'),
    path('guthealth/', other.guthealth, name='guthealth'),

    path('forum/', forum.forum, name='forum'),
    path('forums/<int:id>', forum.viewforum, name='viewforum'),
    path('newpost/', forum.newpost, name='newpost'),
    path('viewpost/<int:post_id>', forum.viewpost, name='viewpost'),
]
