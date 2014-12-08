# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from control import views

urlpatterns = [  

    url(r'^$', views.index, name='index'), 
    url(r'^chklogin$', views.chklogin, name='chklogin'),
    url(r'^prospanel$', views.prospanel, name='prospanel'),
    
]
