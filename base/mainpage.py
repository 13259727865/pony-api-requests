#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
from play001.base.readyaml import ReadYaml

url_data = ReadYaml().readyaml()

class HttpClient:
	def __init__(self):
		self.host = url_data['address']