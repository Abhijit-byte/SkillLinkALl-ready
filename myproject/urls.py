"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Page routes
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('map/', views.map, name='map'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('swap/', views.swap, name='swap'),
    path('profile/', views.profile, name='profile'), 
    path('feed/', views.feed, name='feed'),
    path('projects/', views.projects, name='projects'),
    path('events/', views.events, name='events'),
    path('explore/', views.explore, name='explore'),
    path('resources/', views.resources, name='resources'),
    path('mybookings/', views.mybookings, name='mybookings'),
    path('credits/', views.credits, name='credits'),
    path('meet', views.meet, name='meet'),
    path('profile3/', views.profile3, name='profile3'),

]
