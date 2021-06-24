#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini


from base import readyaml
from base import mainpage

class Login(mainpage.HttpClient):

    def __init__(self):
        super(Login, self).__init__()
        self.api_url = readyaml.ReadYaml("api", "login_api.yaml").readyaml()
        # self.api_send = HttpClient()

    #登录接口， params：用户名、密码
    def login(self,username,password):
        print("准备登录")
        url = self.api_url["login"]
        method = "post"
        body = {
            "user_name":username,
            "pass_word":password
        }
        return self.send(url=url,method=method,body=body)


if __name__ == '__main__':
    a = Login().login("hanc","NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw==")
    print(a.cookies.get_dict())
    print("测试！")