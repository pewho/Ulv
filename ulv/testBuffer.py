#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parser import Exporter
import uuid

if __name__ == '__main__':
	exp = Exporter('out.csv', ['Id','data1','data2'])
	for x in range(1, 1000):
		exp.writerow({'id':uuid.uuid4(), 'data1':x, 'data2':uuid.uuid1()})