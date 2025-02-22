#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:


from pychrome import Chrome

# 连接到Chrome浏览器
chrome = Chrome()

# 获取书签列表
bookmarks = chrome.get_bookmarks()

# 打印书签列表
for bookmark in bookmarks:
    print(bookmark)

# 关闭Chrome浏览器
chrome.close()
