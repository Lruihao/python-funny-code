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
  "username":"201603010223",
  "password":"052737",
  "action":"signin"
}

daka = {
  "operationType":"Create",
  "sfzx":"0",
  "jzdSheng.dm":"430000",
  "jzdShi.dm":"430500",
  "jzdXian.dm":"430527",
  "jzdDz":"黄桑对河",
  "jzdDz2":"黄桑对河",
  "lxdh":"17352623219",
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
  response1=json.dumps(r1.json(),indent=4,ensure_ascii=False) #sort_keys=True 
  print("登录状态:",r1.status_code)
  print(response1)
  header1 = r1.headers
  headers["Cookie"] = header1["Set-Cookie"]

  # 打卡
  r3 = requests.post(daka_url, data=daka,headers=headers,verify=False)
  response3=json.dumps(r3.json(),indent=4,ensure_ascii=False)
  print("打卡状态:",r3.status_code)
  print(response3)

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
 