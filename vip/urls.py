# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from vip import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^createuser$', views.createuser, name='createuser'),
    url(r'^test$', views.test, name='test'),
    url(r'^account$', views.account, name='account'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login$', views.login, name='login'),
    url(r'^handlelogin$', views.handlelogin, name='handlelogin'),
    url(r'^handledit$', views.handledit, name='handledit'),
    url(r'^howtobuy$', views.howtobuy, name='howtobuy'),
    url(r'^deposit$', views.deposit, name='deposit'),
]
