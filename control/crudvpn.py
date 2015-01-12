# -*- coding: utf-8 -*-
from vip.models import User
from vip.models import GlobVar
import platform
import time
import datetime
# 根据系统类型返回路径


def getppppath():
    ostype = platform.system()
    if ostype == 'Windows':
        return "E:\\usrpas.txt"
    if ostype == 'Linux':
        return "/etc/ppp/chap-secrets"

# 根据账号名删除vpn账号


def delvpnbyname(names):
    f = open(getppppath(), 'r')
    totstr = ''
    curstr = f.readline()
    while curstr != '':
        cur_account = curstr.split()
        deled_fg = 0
        if (len(cur_account) >= 4 and (cur_account[1] == 'pptpd' or cur_account[1] == 'l2tpd')):
            account_name = cur_account[0]

            for name in names:
                if account_name == name:
                    deled_fg = 1
                    break
        if deled_fg == 0:
            totstr += curstr

        curstr = f.readline()
    print totstr
    f.close()
    f = open(getppppath(), 'w+')
    f.write(totstr)
    f.close()

# 根据IP地址删除vpn账号


def delvpnbyipaddr(ipaddrs):
    f = open(getppppath(), 'r')
    totstr = ''
    curstr = f.readline()
    while curstr != '':
        cur_account = curstr.split()
        deled_fg = 0
        if (len(cur_account) >= 4 and (cur_account[1] == 'pptpd' or cur_account[1] == 'l2tpd')):
            account_ipaddr = cur_account[3]            
            for ipaddr in ipaddrs:
                if account_ipaddr == ipaddr:
                    print ipaddr
                    print account_ipaddr
                    deled_fg = 1
                    break
        if deled_fg == 0:
            totstr += curstr

        curstr = f.readline()
    print totstr
    f.close()
    f = open(getppppath(), 'w+')
    f.write(totstr)
    f.close()


# IP地址 数字型转化为字符型


def inttoipstr(ival):
    retstr = [0, 0, 0, 0]
    for i in range(4):
        retstr[i] = str(ival % 256)
        ival /= 256
    return retstr[3] + '.' + retstr[2] + '.' + retstr[1] + '.' + retstr[0]

# 删除available_days=0的账号  给available_days>0的添加账号


def check():
    all_user_list = User.objects.all()
    need_account_list = all_user_list.filter(available_days=0)
    del_names = []
    for cur_account in need_account_list:
        del_names.append(cur_account.username)
    delvpnbyname(del_names)
    need_account_list = all_user_list.filter(available_days__gt=0)
    for need_account in need_account_list:
        addvpnaccount(need_account.username, need_account.password, 'pptp')

    print del_names
    print need_account_list


# 添加VPN账号

def addvpnaccount(vpnusr, vpnpas, vpntype):
    f = open(getppppath(), 'a+')
    curstr = f.readline()
    name_dict = {}
    ipaddr_dict = {}
    del_ipaddrs = []
    retval = 1
    # initial ip addr vis array
    while (curstr != ''):
        print curstr
        cur_account = curstr.split()
        if (len(cur_account) >= 4 and (cur_account[1] == 'pptpd' or cur_account[1] == 'l2tpd')):
            account_name = cur_account[0]
            account_type = cur_account[1]
            account_pass = cur_account[2]
            # ip addr
            account_ipaddr = 0
            deled_fg = 0
            for curatom in cur_account[3].split('.'):
                print curatom
                account_ipaddr *= 256
                account_ipaddr += int(curatom)
            print account_ipaddr
            if not (account_name in name_dict):
                print account_name
                name_dict[account_name] = 1
            else:
                del_ipaddrs.append(cur_account[3])
                deled_fg = 1

            if not (account_ipaddr in ipaddr_dict):
                print account_ipaddr
                ipaddr_dict[account_ipaddr] = 1
            else:
                if deled_fg == 0:
                    del_ipaddrs.append(cur_account[3])
        curstr = f.readline()
    if (not (vpnusr in name_dict)):
        if vpntype == 'l2tp':
            for i in range(167837954, 167838208):
                # print i
                if not (i in ipaddr_dict):
                    f.seek(0)
                    f.seek(0, 2)
                    f.write(
                        vpnusr + ' ' + vpntype + 'd ' + vpnpas + ' ' + inttoipstr(i) + '\n')
                    print(
                        vpnusr + ' ' + vpntype + 'd ' + vpnpas + ' ' + inttoipstr(i) + '\n')
                    break
        if vpntype == 'pptp':
            for i in range(167838210, 167838464):
                # print i
                if not (i in ipaddr_dict):
                    f.seek(0)
                    f.seek(0, 2)
                    f.write(
                        vpnusr + ' ' + vpntype + 'd ' + vpnpas + ' ' + inttoipstr(i) + '\n')
                    print(
                        vpnusr + ' ' + vpntype + 'd ' + vpnpas + ' ' + inttoipstr(i) + '\n')
                    break
    else:
        retval = 0
    f.close()
    delvpnbyipaddr(del_ipaddrs)
    return retval




# 改变VPN类型


def updatevpnaccount(vpnusr, vpnpas, vpntype):
    delvpnbyname([vpnusr])
    addvpnaccount(vpnusr, vpnpas, vpntype)

def loopwork():
    fgobj = GlobVar.objects.all()[0]
    fgobj.currentfg = True
    fgobj.save()
    print fgobj.autosubavday
    try:
        while fgobj.autosubavday:
            print fgobj.autosubavday
            all_user_list = User.objects.all()
            needchg_account_list = all_user_list.filter(available_days__gt=0)
            for needchg_account in needchg_account_list:
                needchg_account.available_days -= 1
                needchg_account.save()
            time.sleep(15)
            fgobj = GlobVar.objects.all()[0]
    except:
        pass
    fgobj.currentfg = False
    fgobj.save()
    print "end"

if __name__=='__main__':
    loopwork()