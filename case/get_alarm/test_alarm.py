#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
import jsonpath
import pymysql
import pytest
import sys
from os.path import dirname
sys.path.append(dirname(dirname(dirname(__file__))))
from api_action.vehicle_alarm import VehicleAlarm
from base.readyaml import ReadYaml
import allure
data = ReadYaml("data", "login_data.yaml").readyaml()

@allure.feature("报警查询用例类")
class TestAlarm:

    # @pytest.mark.parametrezr("user,pw",data["login"])
    def setup_class(self):
        # con = pymysql.connect(host="127.0.0.1", port=3306, user="dev", password="productdev123")
        # print("链接数据库")
        # self.cur = con.cursor()
        params = data["login"]
        # user = "hanc"
        # pw = "NWVhN3Vtc2RmYnRhZWRtaXBuMDVzcWR6dzZxaWh2cXA4Mw=="
        print(params[0][0], params[0][1])
        self.alarm = VehicleAlarm(params[0][0], params[0][1])

    def teardown_class(self):
        # self.cur.close()
        pass
    @allure.story("时间，车辆输入")
    @pytest.mark.parametrize("start_time,end_time,vehicle_id,count", data["get_alarm"], ids=data["ids"])
    def test_get_alarm(self, start_time, end_time, vehicle_id, count):
        # print(data["get_alarm"])
        r = self.alarm.vehicle_alarm(start_time, end_time, vehicle_id)
        # print(jsonpath.jsonpath(r.json(), "$..count")[0])
        # print(r.json())
        assert r.status_code == 200
        assert jsonpath.jsonpath(r.json(), "$..count")[0] == count
