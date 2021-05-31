#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
import requests

from page import login
from page.login import Login
from page.vehicle_alarm import Alarm


class VehicleAlarm:
    def __init__(self,user,pw):
        #业务接口调用前，获取到登录用户session_id
        self.username = user
        self.password = pw
        self.login_rec = Login()
        self.session = {"cookie": f"ponytech_sid={self.login_r()['ponytech_sid']}"}
        # print(self.session)
        self.alarm_rec = Alarm()

    def login_r(self):
        a = self.login_rec.login(self.username, self.password)
        # print("输出：", a.cookies.get_dict())
        return a.cookies.get_dict()

    def vehicel_alarm(self, start_time, end_time, vehicle_id=[]):
        return self.alarm_rec.get_vehicle_alarm(start_time, end_time, vehicle_id=vehicle_id, headers=self.session)

    def vehicle_alarm_count(self, start_time, end_time, vehicle_list=[]):
        return self.alarm_rec.get_alarm_count(start_time, end_time, vehicle_list=vehicle_list, headers=self.session)


if __name__ == '__main__':
    a = VehicleAlarm("hanc","NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw==")
    r = a.vehicel_alarm(start_time="2021-05-25 00:00:00", end_time="2021-05-25 23:59:59",
                        vehicle_id=["242", "187", "199"])
    print(r.json())
    r1 = a.vehicle_alarm_count(start_time="2021-05-25 00:00:00", end_time="2021-05-25 23:59:59",
                               vehicle_list=["242", "187", "199"])
    print(r1.json())
