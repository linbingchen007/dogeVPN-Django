# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django.core.context_processors import csrf
import time

# Create your views here.


def index(request):    
    c = {}
    c.update(csrf(request))
    return render_to_response('control/index.html',c)

def panel(request):
    return render(request, 'control/panel.html')

def chklogin(request):
    userstr = request.POST['username']
    passstr = request.POST['password']
    if (userstr == 'linbingchen' and passstr == '123456'):
        return panel(request)
    content = {
            'errinf': "登录失败",
        }
    return render(request, 'control/error.html',content)

def prospanel(request):
    vpn_type_str = request.POST['vpntype']
    fg = 0
    if vpn_type_str == 'all':
        fg = 0
    elif vpn_type_str == 'pptp':
        fg = 1
    elif vpn_type_str == 'l2tp':
        fg = 2
    else:
        fg = -1
    f = open('/etc/ppp/chap-secrets', 'r')
    curstr = f.readline()
    res_accounts = []
    while (curstr != ''):
        cur_account_list = curstr.split()
        if (len(cur_account_list) >= 4 and ( cur_account_list[1] == 'pptpd' or cur_account_list[1] == 'l2tpd')):
            if (fg == 0):
                res_accounts.append(cur_account_list)
            elif (fg == 1 and cur_account_list[1] == 'pptpd'):
                res_accounts.append(cur_account_list)
            elif (fg == 2 and  cur_account_list[1] == 'l2tpd'):
                res_accounts.append(cur_account_list)
            else:
                pass
        curstr = f.readline()
    content = {"vpn_account_list":res_accounts,
                "fuc":"tst",
            }
    f.close()
    return render(request, 'control/panel.html', content)
