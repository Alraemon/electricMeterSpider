#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 19:52:36 2018

This script is for analyzing the data acquired meterSpider.py
Need meterData.data to proceed

@author: erwin
"""

import numpy as np
import scipy as sp
import pickle
import matplotlib.pyplot as plt

file=open("meterData.data","rb")
raw_elec=pickle.load(file)
file.close()
file=open("temperature.data","rb")
raw_temp=pickle.load(file)
file.close()
elec_list=[]
temp_list=[]
for i in range(299):
    day_elec=0
    for j in range(210):
        day_elec+=float(raw_elec[j][i][1])
    elec_list.append(day_elec)
for i in range(299):
    temp_list.append(float(raw_temp[i][1]))
elec=np.array(elec_list[:-2])
temp=np.array(temp_list[:-2])
date=[]
for i in range(299):
    #date_1=dt.date(int(raw_temp[i][0][0:4]),int(raw_temp[i][0][5:7]),int(raw_temp[i][0][8:10]))
    date_1=raw_temp[i][0]
    date.append(date_1)
plt.plot(date[:-2],elec,"r.")
tick=list(range(0,297,37))
plt.xticks(tick,date[-1:0:-37],rotation=20)
plt.xlabel("Date")
plt.ylabel("Electricity Consumption (KWh)")
plt.title("Relation between date and electricity")
plt.show()

def f(temp_x,a,b,c):
    return a*np.power(temp_x,2)+b*temp_x+c

popt,pcov=sp.optimize.curve_fit(f,temp,elec)
plt.plot(temp,elec,"b.")
x=np.linspace(0,40,1000)
plt.plot(x,popt[0]*np.power(x,2)+popt[1]*x+popt[2],'r-')
plt.xlabel("Temperature (℃)")
plt.ylabel("Electricity Consumption (KWh)")
plt.title("Relation between local temperature and electricity")
plt.show()
print("\033[1;35m The fitted curve is:  \033[0m","E=",str(popt[0]),"t^2+",str(popt[1]),"t+",str(popt[2]))