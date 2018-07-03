#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 18:57:26 2018

This script is for getting all the options info on the Default.aspx
And save options info file with pickle.

@author: erwin
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pickle

browser=webdriver.PhantomJS()
print("\033[1;35m //PhantomJS Browser Constructed// \033[0m")
browser.get("http://202.120.163.129:88/Default.aspx")
print("\033[1;35m //Connection Opened// \033[0m")
option_set=[]
print("\033[1;35m //Crawling Data...// \033[0m")
select_1=Select(browser.find_element_by_id('drlouming'))
options_1=select_1.options
for num1 in [2]:
#for num1 in range(1,len(options_1)):
    name_1=options_1[num1].text
    print(options_1[num1].text)
    value_1=options_1[num1].get_attribute("value")
    select_1.select_by_index(num1)
    time.sleep(1)
    select_2=Select(browser.find_element_by_id("drceng"))
    options_2=select_2.options
    for num2 in [16]:
    #for num2 in range(1,len(options_2)):
        name_2=name_1+options_2[num2].text
        print(options_2[num2].text)
        value_2=options_2[num2].get_attribute("value")
        select_2.select_by_index(num2)
        time.sleep(1)
        select_3=Select(browser.find_element_by_id("dr_ceng"))
        options_3=select_3.options
        if len(options_3)>1:
            for num3 in range(1,len(options_3)):
                name_3=name_2+options_3[num3].text
                print(options_3[num3].text)
                value_3=options_3[num3].get_attribute("value")
                select_3.select_by_index(num3)
                time.sleep(1)
                select_4=Select(browser.find_element_by_id("drfangjian"))
                options_4=select_4.options
                if len(options_4)>1:
                    for option_4 in options_4[1:]:
                        name_4=name_3+option_4.text
                        print(option_4.text)
                        value_4=option_4.get_attribute("value")
                        select_4.select_by_value(value_4)
                        option_data={"drlouming":value_1,"drceng":value_2,\
                                     "dr_ceng":value_3,"drfangjian":value_4,\
                                     "radio":"usedR"}
                        option_set.append([name_4,option_data])
                    select_3=Select(browser.find_element_by_id("dr_ceng"))
                    options_3=select_3.options
                else:
                    value_4=options_4[0].get_attribute("value")
                    select_4.select_by_value(value_4)
                    option_data={"drlouming":value_1,"drceng":value_2,\
                                 "dr_ceng":value_3,"drfangjian":value_4,\
                                 "radio":"usedR"}
                    option_set.append([name_3,option_data])
                    select_3=Select(browser.find_element_by_id("dr_ceng"))
                    options_3=select_3.options
        else:
            select_4=Select(browser.find_element_by_id("drfangjian"))
            options_4=select_4.options
            name_3=''
            for option_4 in options_4[1:]:
                name_4=name_3+option_4.text
                print(option_4.text)
                value_3=options_3[0].get_attribute("value")
                value_4=option_4.get_attribute("value")
                select_4.select_by_value(value_4)
                option_data={"drlouming":value_1,"drceng":value_2,\
                             "dr_ceng":value_3,"drfangjian":value_4,\
                             "radio":"usedR"}
                option_set.append([name_4,option_data])
        select_2=Select(browser.find_element_by_id("drceng"))
        options_2=select_2.options
        time.sleep(1)
    select_1=Select(browser.find_element_by_id('drlouming'))
    options_1=select_1.options
    time.sleep(1)
print("\033[1;35m //Data Crawled// \033[0m")
file=open("info.data","wb")
pickle.dump(option_set,file)
file.close()
print("\033[1;35m //Data Saved to info.data// \033[0m")
browser.quit()