#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
from bs4 import BeautifulSoup
import re
import io

with open('result.csv') as csvfile:
	with open('newresult.csv', 'w', newline='') as newcsvf:
		result = csv.reader(csvfile)
		iterre = iter(result)
		next(iterre)
		for row in iterre:
			filename = re.sub("Des.*ment/", "", row[1])
			print(filename)
			soup = BeautifulSoup(io.open(filename, encoding='ISO-8859-1'))
			t00 = soup.title
			
			if t00:
				t0 = t00.string
				print(t0)
				t1 = re.sub('^review for', '', t0.lower())
				t2 = re.sub('\(\d+\)?', '', t1).strip()
				#print(t2)
				row.append(t2)
				#print(row)
				spamWriter = csv.writer(newcsvf)
				spamWriter.writerow(row)