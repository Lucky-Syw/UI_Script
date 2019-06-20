#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:lucky,time:2019-06-20
from log.logs import logging

class instructions:

	@staticmethod
	def info(msg = None):
		def out_wapper(func):
			def wapper(*wargs,**kwargs):
				logging.info("开始执行：***************"+msg+"***********")
				func(*wargs,**kwargs)
				logging.info("执行结束：***************"+msg+"***********")
			return wapper
		return out_wapper