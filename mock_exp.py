#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def send_request(url):
    r = requests.get(url)
    return r.status_code


def get_result():
    return send_request('http://www.ustack.com')
