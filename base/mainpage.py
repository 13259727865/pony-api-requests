#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini

import json
import requests
from base.readyaml import ReadYaml

#实例化读取配置文件对象
# from page.login import Login

url_data = ReadYaml().readyaml()



class HttpClient:


    def __init__(self):
        self.session = requests.session()
        # self.session.cookies = Login.login()
        #拼接url和端口
        self.host = 'http://'+url_data['address']['host']+':'+str(url_data['address']['port'])
        #默认请求头
        self.default_head = {
            "Content-Type": "application/json"
        }


    def send(self,url,method='get',headers={},body={},sid=False):
        """
        请求接口方法
        :return: 接口response所有内容
        """
        # print("输出：",headers)
        com_url = self.host+url
        headers.update(self.default_head)
        # print(com_url,headers,body)
        # print(com_url, headers, body,method)
        if method =="get":
            if sid:
                # r = self.session.
                pass
            else:
                r = requests.get(url=com_url,headers=headers,params=body)
            # return r.json()
        elif method=="post":

            r = requests.post(url = com_url,headers=headers,json=body)
        return r
    



if __name__ == '__main__':
    a = HttpClient()
    b = a.send(url="/ponysafety2/login",method="post",body={"user_name":"hanc","pass_word":"NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw=="})
    print(b.status_code)