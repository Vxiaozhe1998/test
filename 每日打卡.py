import requests
import time
session = requests.Session()
host = r"http://xuegong.qfnu.edu.cn:8080"
login_url = host + r"/authentication/login"
user_info_url = host + r"/info/current"
morning_url = host + r"/student/healthInfo/save"
night_url = host + r"/student/healthInfoNoon/save/晚上/36.5"
noon_url = host + r"/student/healthInfoNoon/save/中午/36.2"

headers = {
    'user-agent': 'Dart/2.9 (dart:io)'
}
user_info_json = {
    'username': '2018416061',
    'password': '295410',
    'type': 'student',
}
health_info = {
    "home": "在校",
    "address": "",
    "keepInHome": "否",
    "keepInHomeDate": "null",
    "keepInHomeReasonSite": "",
    "contact": "否",
    "contactType": "",
    "infect": "否",
    "infectType": "",
    "infectDate": "",
    "familyNCP": "否",
    "familyNCPType": "",
    "familyNCPDate": "",
    "familyNCPRelation": "",
    "cold": "否",
    "fever": "否",
    "feverValue": "",
    "cough": "否",
    "diarrhea": "否",
    "homeInHubei": "否",
    "arriveHubei": "无",
    "travel": "无",
    "remark": "无",
    "submitCount": 1,
    "contactDetail": "",
    "location": "山东省日照市东港区学林路158号",
    "naDetection": "否",
    "areaInfect": "否",
    "areaInfectType": "",
    "areaInfectDate": "",
    "areaInfectNumber": "",
    "contactAH": "否",
    "contactAHDetail": "",
    "outProvinceBack14": "未出省",
    "naDetectionDate": "",
    "pharynxResult": "",
    "anusResult": "",
    "saDetection": "否",
    "lgMResult": "",
    "lgGResult": "",
    "saDetectionDate": ""
}


# 登陆
response_login = session.post(url=login_url, json=user_info_json, headers=headers)



# 用户信息
response_user_info = session.post(url=user_info_url, headers=headers)



headers = {
    'user-agent': 'Dart/2.9 (dart:io)', 
    'authorization': session.cookies['syt.sessionId']
}


t = int(time.strftime("%H", time.localtime()))
if t < 11:
    # 早上提交
    response_morning = session.post(url=morning_url, json=health_info, headers=headers)
    #response_morning.json()
elif t < 17:
    # 中午提交
    response_noon = session.post(url=noon_url, headers=headers)
   # response_noon.json()
else:
    # 晚上提交
    response_night = session.post(url=night_url, headers=headers)
   # response_night.json()

