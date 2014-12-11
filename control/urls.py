# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from control import views

urlpatterns = [  

    url(r'^$', views.index, name='index'), 
    url(r'^chklogin$', views.chklogin, name='chklogin'),
    url(r'^prospanel$', views.prospanel, name='prospanel'),
    url(r'^del/(?P<del_ipaddr>[0-9.]+)/(?P<last_type>[a-zA-Z0-9]+)/$', views.operdel, name='operdel'),    
    url(r'^refreshvpn$', views.refreshvpn, name='refreshvpn'),
    url(r'^operchg/(?P<usr_name>[a-zA-Z0-9]+)/(?P<last_type>[a-zA-Z0-9]+)/(?P<usr_type>[a-zA-Z0-9]+)/(?P<usr_pas>[a-zA-Z0-9]+)/$', views.operchg, name='operchg'),    
    
]
