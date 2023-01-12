#  !/usr/bin/env python
#  -*- coding: utf-8 -*-
#  @author : Ye Yuhao
#  @Time   : 2023/1/11 21:45
#  @File   : just for fun
#  @annotation : If have any proplem or somewhat wanna to chat,please feel free to e-maill me
#  @address    : milesyeyuhao@gmail.com


#import package
import time
from wxauto import *
import datetime

#customized Functions
def get_time():
    """return the minutes"""
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return now_time.split(" ")[1].split(":")[1]

def time2message2object(msg_object,msg_info,msg_time):
    """timed message delivery"""
    WX = WeChat()
    # WX.ChatWith(msg_object)
    # WX.SendMsg(msg_info)
    if msg_time == "56":
        WX.ChatWith(msg_object)
        WX.SendMsg(msg_info)
        signal_send = "1"
    else:
        signal_send = "waiting"
    return signal_send

#run
if __name__ == "__main__":
    msg_info = u"请问，您有收到上面几句话了吗？"
    msg_object = u"曹诗林"
    print("working")
    while True:
        msg_time = get_time()
        signal_send = time2message2object(msg_object, msg_info, msg_time)
        if signal_send == "1":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("send sucessfully!")
        else :
            print("waiting")

        time.sleep(60)


