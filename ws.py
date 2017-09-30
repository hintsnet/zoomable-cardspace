#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin, stdout

# d3_json_obj = {}
# 从 STDIN 获取一行输入 "张三"，以 "你好，张三!" 响应给客户端
while True:
  line = stdin.readline().strip()
  #json_obj = parseJSON(json_str)
  #d3_data = d3ify(json_obj)
  print('你好，%s！' % line)
  stdout.flush() # Remember to flush

