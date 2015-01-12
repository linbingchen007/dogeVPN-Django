# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django.core.context_processors import csrf
from vip.models import User
import time
import control.crudvpn
import platform
from vip.models import GlobVar
from control import crudvpn
# Create your views here.
control_usr = 'linbingchen'
control_pwd = '123456'


def getppppath():
    ostype = platform.system()
    if ostype == 'Windows':
        return "E:\\usrpas.txt"
    if ostype == 'Linux':
        return "/etc/ppp/chap-secrets"


def index(request):    
    c = {}
    c.update(csrf(request))
    return render_to_response('control/index.html',c)

def panel(request):
    return render(request, 'control/panel.html')



def operdel(request, del_ipaddr, last_type):
    crudvpn.delvpnbyipaddr([del_ipaddr])
    return prospanel(request, vpn_type_str = last_type)

def refreshvpn(request):    
    crudvpn.check()
    return prospanel(request,  'all')


#def updatevpnaccount(vpnusr, vpnpas, vpntype):
def operchg(request, usr_name, last_type, usr_type, usr_pas):
    if usr_type == 'l2tpd':
        usr_type = 'pptp'
    else:
        usr_type = 'l2tp'
    crudvpn.updatevpnaccount(usr_name, usr_pas, usr_type)
    return prospanel(request,  last_type)

def chklogin(request):
    userstr = request.POST['username']
    passstr = request.POST['password']
    if (userstr == control_usr and passstr == control_pwd):
        request.session['adminusr'] = userstr
        request.session['adminpsw'] = passstr
        return panel(request)
    content = {
            'errinf': "登录失败",
        }
    return render(request, 'control/error.html',content)

def prospanel(request, vpn_type_str = 'null' ):
    try :
        if (not (request.session['adminusr'] == control_usr and request.session['adminpsw'] == control_pwd)):
            content = {
             'errinf': "登录失败",
            }
            return render(request, 'control/error.html',content)
    except:
        content = {
             'errinf': "未知错误",
            }
        return render(request, 'control/error.html',content)
    if vpn_type_str == 'null':
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
    f = open(getppppath(), 'r')
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
                "last_type":vpn_type_str,
            }
    f.close()
    return render(request, 'control/panel.html', content)

def state(request):
    fgobj = GlobVar.objects.all()[0]
    return HttpResponse(unicode(fgobj.currentfg))


def switch(request):
    fgobj = GlobVar.objects.all()[0]
    if not fgobj.currentfg:
        fgobj.autosubavday = True
        fgobj.save()
        crudvpn.loopwork()
    else:
        fgobj.autosubavday = False
        fgobj.save()
    fgobj = GlobVar.objects.all()[0]
    return HttpResponse(unicode(fgobj.currentfg))