#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 21:13:32 2018

Use Weather API to get temperature data of Shanghai in last one year
And save it to temperature.data

@author: erwin
"""

import requests
import time
import pickle

dataset=[]
raw_today=requests.get("http://v.juhe.cn/weather/index?cityname=%E8%8B%8F%E5%B7%9E&key=bf80f61ebf0912e91f7606f9d043a55d")
j_today=raw_today.json()
data_today=[time.strftime('%Y-%m-%d',time.localtime(time.time())),j_today["result"]["today"]["temperature"][-3:-1]]
dataset.append(data_today)
for i in range(1,299):
    param={"key":"b0c4e54a67fa64878b39648a2c26a9c7","city_id":"1844",\
           "weather_date":time.strftime('%Y-%m-%d',time.localtime(time.time()-24*3600*i))\
           }
    raw_res=requests.get("http://v.juhe.cn/historyWeather/weather",params=param)
    j_res=raw_res.json()
    data=[j_res["result"]["weather_date"],j_res["result"]["day_temp"][:-1]]
    dataset.append(data)
    time.sleep(0.5)
file=open("temperature.data","wb")
pickle.dump(dataset,file)
file.close()
