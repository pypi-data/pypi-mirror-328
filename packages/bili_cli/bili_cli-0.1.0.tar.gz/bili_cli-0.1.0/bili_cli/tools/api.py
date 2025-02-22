#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import requests


class ScheApi():
    class Meta():
        HTTP = "http://localhost:8008"

    @classmethod
    def default(cls) -> 'ScheApi':
        return ScheApi()

    def build_url(self, path):
        return self.Meta.HTTP + path

    def get(self, path, params={}):
        return requests.get(self.build_url(path), params=params)
