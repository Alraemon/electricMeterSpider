#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:36:30 2018

@author: erwin
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pickle

file=open("info.data","rb")
option_set=pickle.load(file)
file.close()
print("\033[1;35m //Loaded Meters Info from file// \033[0m")
browser=webdriver.PhantomJS()
print("\033[1;35m //PhantomJS Browser Constructed// \033[0m")
print("\033[1;35m //Begin Iteration...// \033[0m")
data_matrix=[]
date_start=time.strftime('%Y-%m-%d',time.localtime(time.time()-31536000))
date_end=time.strftime('%Y-%m-%d',time.localtime(time.time()))
try:
    for option in option_set:
        browser.get("http://202.120.163.129:88/Default.aspx")
        select_1=Select(browser.find_element_by_id("drlouming"))
        select_1.select_by_value(option[1]["drlouming"])
        time.sleep(0.2)
        select_2=Select(browser.find_element_by_id("drceng"))
        select_2.select_by_value(option[1]["drceng"])
        time.sleep(0.2)
        select_2=Select(browser.find_element_by_id("drceng"))
        select_2.select_by_value(option[1]["drceng"])
        time.sleep(0.2)
        select_3=Select(browser.find_element_by_id("dr_ceng"))
        select_3.select_by_value(option[1]["dr_ceng"])
        time.sleep(0.2)
        select_4=Select(browser.find_element_by_id("drfangjian"))
        select_4.select_by_value(option[1]["drfangjian"])
        time.sleep(0.2)
        checkbox=browser.find_element_by_id("usedR")
        checkbox.click()
        time.sleep(0.2)
        submit_1=browser.find_element_by_id("ImageButton1")
        submit_1.click()
        time.sleep(0.2)
        print("\033[1;35m Iteration Process: \033[0m"+option[0])
    
        date_1=browser.find_element_by_id("txtstart")
        date_1.clear()
        date_1.send_keys(date_start)
        date_2=browser.find_element_by_id("txtend")
        date_2.clear()
        date_2.send_keys(date_end)
        submit_2=browser.find_element_by_id("btnser")
        submit_2.click()
        data_set=[]
        for j in range(2,12):
            data_date=browser.find_element_by_xpath("//table/tbody/tr["+str(j)+"]/td[1]")
            data_usage=browser.find_element_by_xpath("//table/tbody/tr["+str(j)+"]/td[3]")
            data=[data_date.text,data_usage.text]
            data_set.append(data)
        for i in range(2,31):
            browser.get("http://202.120.163.129:88/usedRecord1.aspx?p="+str(i))
            if i!=30:
                for j in range(2,12):
                    data_date=browser.find_element_by_xpath("//table/tbody/tr["+str(j)+"]/td[1]")
                    data_usage=browser.find_element_by_xpath("//table/tbody/tr["+str(j)+"]/td[3]")            
                    data=[data_date.text,data_usage.text]
                    data_set.append(data)
            else:
                for j in range(2,11):
                    data_date=browser.find_element_by_xpath("//table/tbody/tr["+str(j)+"]/td[1]")
                    data_usage=browser.find_element_by_xpath("//table/tbody/tr["+str(j)+"]/td[3]")            
                    data=[data_date.text,data_usage.text]
                    data_set.append(data)
        data_matrix.append(data_set)
    print("\033[1;35m //Iteration Complete// \033[0m")
except:
    print(browser.page_source)
    print("\033[1;35m //Iteration Abort// \033[0m")  
finally:
    meter_file=open("meterData.data","wb")
    pickle.dump(data_matrix,meter_file)
    meter_file.close()
    print("\033[1;35m //Data File saved to meterData.data// \033[0m")
    browser.close()