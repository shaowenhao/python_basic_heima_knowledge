# _*_ coding: UTF-8 _*_
# 开发人员 : z00498ta
# 开发时间 : 3/10/2023 2:41 PM
# 文件名称: 多线程编程.PY
import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':

    # 逗号加上才表示元组
    sing_thread = threading.Thread(target=sing,args=("我要唱歌",))
    dacne_thread = threading.Thread(target=dance,kwargs={"msg":"我要跳舞"})

    sing_thread.start()
    dacne_thread.start()