"""nowtifydjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from . import views


urlpatterns = patterns('',
                       url(r'^admin/', admin.site.urls),
                       url(r'^$', views.custom_login, name='custom_login'),
                       url(r'^login/', views.login, name='login'),
                       url(r'^authentication/', views.authentication, name='authentication'),
                       url(r'^change-password/', views.change_password, name='change_password'),
                       url(r'^index/', views.index, name='index'),
                       url(r'^overview/', views.overview, name='overview'),
                       url(r'^sensor/', views.sensor, name='sensor'),
                       url(r'^logout/', views.logout, name='logout'),
                       url(r'^wearable/', views.wearable, name='wearable'),
                       url(r'^dashboard/', views.dashboard, name='dashboard'),
                       url(r'^wearable/', views.wearable, name='wearable'),
                       url(r'^dashboard/', views.dashboard, name='dashboard'),
                       url(r'^change_password/', views.settings, name='settings'),
                       url(r'^alert/', views.alert, name='alert')

# nowtifydjango2 Pages
                       # url(r'^overview/', views.index, name='overview'),
                       # url(r'^/user', views.user, name='user'),
                       # url(r'^sensor/', views.sensor, name='sensor'),
                       # url(r'^wearable/', views.wearable, name='wearable'),
                       # url(r'^dashboard/', views.dashboard, name='dashboard')

                       )