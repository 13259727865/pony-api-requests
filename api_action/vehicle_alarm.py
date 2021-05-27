#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import requests

from page import login
from page.login import Login
from page.vehicle_alarm import Alarm


class VehicleAlarm:
    def __init__(self):
        self.username = "hanc"
        self.password = "NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw=="
        self.login_rec = Login()
        self.session = {"cookie":f"ponytech_sid={self.login_r()['ponytech_sid']}"}
        print(self.session)
        self.alarm_rec = Alarm()


    def login_r(self):
        a = self.login_rec.login(self.username,self.password)
        print("输出：",a.cookies.get_dict())
        return a.cookies.get_dict()

    def vehicel_alarm(self,start_time, end_time,vehicle_id=[]):
        return  self.alarm_rec.get_vehicle_alarm(start_time,end_time,vehicle_id=vehicle_id,headers=self.session)

    def vehicle_alarm_count(self):
        pass




if __name__ == '__main__':
    a = VehicleAlarm()
    r = a.vehicel_alarm(start_time="2021-05-25 00:00:00", end_time="2021-05-25 23:59:59",
                                  vehicle_id=["25526", "12910", "25534", "25533"])
    print(r.json())
