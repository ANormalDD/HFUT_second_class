import requests
import json
import time
import os

file = open("user.txt","r")
secret = file.readline().replace('\n',"")
key_session = file.readline()
file.close()
print(secret)
print(key_session)
page_headers = {
    "Host": "dekt.hfut.edu.cn",
    "Connection": "keep-alive",
    "key_session": key_session,
    "xweb_xhr": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8519",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Language": "*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx1e3feaf804330562/91/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}

question_headers = {
    "Host": "dekt.hfut.edu.cn",
    "Connection": "keep-alive",
    "secret": secret,
    "key_session": key_session,
    "xweb_xhr": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8519",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Language": "*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx1e3feaf804330562/91/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}

answer_headers = {
    "Host": "dekt.hfut.edu.cn",
    "Connection": "keep-alive",
    "key_session": key_session,
    "xweb_xhr": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8519",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Language": "*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx1e3feaf804330562/91/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}

data = {
    "category": "",
    "columnType": "0"
}
for page_num in range(1, 36):

    url = f"https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/page/{page_num}/10"
    response = requests.post(url, headers=page_headers, data=json.dumps(data))
    page_data = response.json()

    for question in page_data["data"]["list"]:

        if (question["correct"] == "已完成"):
            continue

        question_id = question["id"]
        url = f"https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/questions/{question_id}"
        time.sleep(1)
        response = requests.get(url, headers=question_headers)
        question_detail = response.json()

        if(("data" not in question_detail) or ("questions" not in question_detail["data"]) or ()):
            continue
        if(question_detail["data"]["todayReach"]):
            exit() #达到每日上限
        for question in question_detail["data"]["questions"]:

            if(question["queType"]): #只做单选题
                continue
            sbid = question["id"]

            for option in question["optionList"]:

                option_id = option["id"]
                url = f"https://dekt.hfut.edu.cn/scReports/api/wx/netlearning/answer/{sbid}"
                time.sleep(1)
                data = [option_id]
                response = requests.post(url, headers=answer_headers, json=data)
                recv_data = response.json()
                if recv_data["data"]["desc"] == "恭喜,获得积分":
                    break