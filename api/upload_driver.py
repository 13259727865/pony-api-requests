#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
from base import mainpage
from base.readyaml import ReadYaml


class UploadDriver(mainpage.HttpClient):
    def __init__(self):
        super(UploadDriver, self).__init__()
        self.api = ReadYaml().readyaml