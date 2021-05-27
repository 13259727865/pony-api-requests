#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import json
import os

import yaml

#读取yaml文件
class ReadYaml:

    def __init__(self,filetype='address',filename=None):
        """params:
        filetype:'address'-default,api,data
        filename:api\data类型需要填写filename
        """

        if filetype == 'address':
            self.path = os.path.dirname(os.path.dirname(__file__))+"/yaml/config/address.yaml"
        elif filetype == 'api':
            self.path = os.path.dirname(os.path.dirname(__file__))+"/yaml/api/"+filename
        elif filetype == 'data':
            self.path = os.path.dirname(os.path.dirname(__file__))+"/yaml/data/"+filename
        else:
            print("未找到对应类型："+filetype)

    def readyaml(self):
        """
        :return:读取对应yaml文件内容为python数据类型
        """
        try:
            with open(self.path,"r",encoding="utf-8")as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print("no sush file")
        except:
            print("参数有误！！")






if __name__ == '__main__':
    a = ReadYaml('address')
    a.readyaml()