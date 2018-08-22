# -*- coding:utf-8 -*-
from urllib2 import urlopen
from json import load
# from ali_rds_get_public_ip import alis
# from func_ali_sz_change_ip import *
import re
import threading
def get_public_ip():
    try:
        my_ip = urlopen('http://ip.42.pl/raw').read()
        # print my_ip
    except:
        try:
            my_ip = load(urlopen('http://jsonip.com'))['ip']
            # print my_ip
        except:
            my_ip = "sorry!!don't get public ip"
    return my_ip

def get_ali_rds_ip():
    ali = alis('ACCESSKEY', 'ACCESSSECERT', 'cn-hangzhou')  # 需改为华东1（cn-hangzhou)
    clt = ali.clt()
    ask = ali.describeDBInstanceIPArrayListRequest('rm-bp1m138ik7m9s03dq')  #查看白名单
    req = clt.do_action_with_exception(ask)
    ali_ip = re.findall(r'"SecurityIPList":"(.*?)"', req)[0]
    return ali_ip

def compare_ip():
    if get_public_ip() == get_ali_rds_ip() :
        print get_public_ip()
        print get_ali_rds_ip()
        print "OK"
    else:
        # func_ali_sz_revoke_IP(old_ip)
        # func_ali_sz_add_IP(new_ip)
        print "NO"
    timer = threading.Timer(5.0, compare_ip)
    timer.start()
if __name__ == "__main__":
    # new_ip = get_public_ip()
    # print new_ip
    # old_ip = get_ali_rds_ip()
    # print old_ip
    # compare_ip()
    timer = threading.Timer(5.0, compare_ip)
    timer.start()
    
