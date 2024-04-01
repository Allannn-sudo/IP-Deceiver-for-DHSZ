
import requests
import time
import os

list1 = ["|","/","-","\\"]
lenth = 4
count = 0

while True:
    #click = {'onclick' : 'logout()'}
    url = "http://1.2.3.4/ajaxlogout?_t=1619144474245"
    res = requests.get(url)#,data = click)
    if str(res) == "<Response [200]>":
        os.system("cls")
        print("Log out success!",list1[count%lenth])
        count = count + 1
    else:
        print("Log out failed")
    #time.sleep(0.1)
    time.sleep(0.005)

