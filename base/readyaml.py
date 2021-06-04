#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import json
import os
import allure
import yaml

#读取yaml文件
class ReadYaml:

    def __init__(self,filetype='address',filename=None):
        """params:
        filetype:'address'-default,api,data
        filename:api\data类型需要填写filename
        """
        with allure.step(f"读取{filetype,filename}"):
            if filetype == 'address':
                self.path = os.path.dirname(os.path.dirname(__file__))+"/yaml/config/address.yaml"
            elif filetype == 'api':
                self.path = os.path.dirname(os.path.dirname(__file__))+"/yaml/api/"+filename
            elif filetype == 'data':
                self.path = os.path.dirname(os.path.dirname(__file__))+"/yaml/data/"+filename
            else:
                print("未找到对应类型："+filetype)


    @allure.story("读取yaml")
    def readyaml(self):
        """
        :return:读取对应yaml文件内容为python数据类型
        """
        try:
            with open(self.path,"r",encoding="utf-8")as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("no sush file")
        except yaml.parser.ParserError:
            print("yaml文件错误！！")
        except:
            print("参数有误！！",)

    # def dumpyaml(self):
    #     a = {"login":{"user":()}}

a = {"login":[["hanc","admin"],["hanc1","admin"]],
     "get_alarm":[
         ["2021-05-25 00:00:00","2021-05-25 23:59:59",["242", "187", "199"]],
         ["2021-05-26 00:00:00","2021-05-26 23:59:59",["242", "187", "199"]],
         ["2021-05-27 00:00:00","2021-05-27 23:59:59",["242", "187", "199"]]
        ]
     }


if __name__ == '__main__':
    a = ReadYaml(filetype='data',filename="login_data.yaml")
    print(a.readyaml())