#!/usr/bin/python
# encoding=utf-8
import re
import json
import time
import requests
import os,sys
import subprocess
logFile1="/opt/pubtrans/logs/ods-flume/logs/flume.log"
city = sys.argv[1]
def monitorLog(logFile):
    # print'监控的日志文件 是 %s'%logFile
    popen = subprocess.Popen('tail -f '+ logFile,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    pid = popen.pid
    #print 'Popen.pid:'+str(pid)
    while True:
        line=popen.stdout.readline().strip()
# 判断内容是否为空
        if line:
            # print line
            #errorlog = re.findall('The channel is full or unexpected failure',line)
            errorlog = re.findall('The channel is full or unexpected failure',line)
            if errorlog:
                dingdingwarning()
        time.sleep(1)
def dingdingwarning():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=aa79eff6bda10dbc79bf870c2aba8252e5794ffc388d44ac886'  # 钉钉机器人的webhook地址
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    message = city +"flume队列已满,请重启应用."

    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
        "at": {
            "atMobiles": [
                "15888826546"  # 如果需要@某人，这里写他的手机号
            ],
            "isAtAll": 0  # 如果需要@所有人，这些写1
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)

if __name__ == "__main__":
    while True:
        monitorLog(logFile1)
        time.sleep(4*60)

