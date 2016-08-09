#!/usr/bin/env python
#coding:utf-8

# filename: ./router.py
# description: This is file is for router file

import sys

from handler.index import IndexHandler

# avoid chinese annotate bringing about bad tings
reload(sys)
sys.setdefaultencoding('utf-8')

urls = [(r"/", IndexHandler)]