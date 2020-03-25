# coding:utf-8
import requests
import time
import json

login_url = "http://xggl.hnie.edu.cn/website/login" # 登录接口
daka_url = "http://xggl.hnie.edu.cn/content/student/temp/zzdk"  # 打卡接口
# laston_url = "http://xggl.hnie.edu.cn/content/student/temp/zzdk/lastone" # 上次打卡数据GET
 
# 消息头数据
headers = {
  "Host": "xggl.hnie.edu.cn",
  "Connection": "keep-alive",
  "Content-Length": "233",
  "Accept": "*/*",
  "X-Requested-With": "XMLHttpRequest",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  "Origin": "http://xggl.hnie.edu.cn",
  "Referer": "http://xggl.hnie.edu.cn/content/menu/student/temp/zzdk?_t_s_=1585046001170",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
  # "Cookie": "JSESSIONID=1C905138A82C2BF5C155C950A3EFDBFA"
}


login = {
  "username":"2016xxxxxxxx",
  "password":"xxxxxx",
  "action":"signin"
}

daka = {
  "operationType":"Create",
  "sfzx":"0",
  "jzdSheng.dm":"430000",
  "jzdShi.dm":"430500",
  "jzdXian.dm":"430527",
  "jzdDz":"世外桃源村",
  "jzdDz2":"世外桃源村",
  "lxdh":"173xxxx3219",
  "grInd":"0",
  "jcInd":"0",
  "jtqk.dm":"4",
  "brqk.dm":"4",
  "tw":"",
  "bz":"",
  "dm":""
}

def lajaDaka():
  # 登录
  r1 = requests.post(login_url, data=login,headers=headers,verify=False)
  if r1.status_code == 200:
    print(time.strftime("%Y:%m:%d:%H:%M", time.localtime()))
    print(login["username"] + " 登录成功！")
    # 拿到登录后的cookie并添加到header中
    header1 = r1.headers
    headers["Cookie"] = header1["Set-Cookie"]
  else:
    return

  # 打卡
  r2 = requests.post(daka_url, data=daka,headers=headers,verify=False)
  response2=r2.json()
  if r2.status_code != 200:
    print("打卡失败！")
    return
  if response2["result"] == True:
    print("打卡成功！")
  else:
    print(response2["errorInfoList"][0]["message"])

if __name__=="__main__":
  while True:
    now_hour = time.strftime("%H", time.localtime())
    now_min = time.strftime("%M", time.localtime())
    # 设置每天8点发送
    if now_hour < "08":
      rest = 8 - int(now_hour)
      sleeptime = (rest-1)*3600 + (60-int(now_min))*60
      print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t脚本将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后打卡")
      time.sleep(sleeptime)
    elif now_hour > "08":
      rest = 8 - int(now_hour) + 24
      sleeptime = (rest-1)*3600 + (60-int(now_min))*60
      print("启动时北京时间为："+time.strftime("%H:%M", time.localtime()),"\t脚本将在",rest-1,"小时",int((sleeptime-(rest-1)*3600)/60),"分钟后打卡")
      time.sleep(sleeptime)
    elif now_hour == "08":
      print("软件明天开始将在每天8点发送数据！")
      lajaDaka()
      time.sleep(24*60*60-int(now_min)*60)
 