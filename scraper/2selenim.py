from distutils.command.build_scripts import first_line_re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome('E:\chromedriver.exe')
browser.get('https://proshore.eu/resources/')

items = []
des = []
rt = []
dg = []
an = []
img = []

last_height = browser.execute_script("return document.body.scrollHeight")
itemTargetCount = 100
while itemTargetCount > len(items):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    time.sleep(5)
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    elements = browser.find_elements(By.CSS_SELECTOR, "#post-836 > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-3f0c3c1f.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > div > div.playground-list-wrapper > div.playground-list.playground-list-max-3 > div")
    name = []
    desc = []
    rtime = []
    desig = []
    aname = []
    imag = []

    for x in range(1, 35):
        for element in elements:
            try:
                title = element.find_element(By.TAG_NAME, 'h4').text
                name.append(title)
                items = name
            except:
                title = 'title'
                items.append(title)

            try:
                description = element.find_element(
                    By.CLASS_NAME, 'playground-excerpt').text
                desc.append(description)
                des = desc
            except:
                description = 'description'
                des.append(description)

            try:
                readtime = element.find_element(
                    By.XPATH, f"(//span[@class='playground-read-time-text'])[{x}]").text
                rtime.append(readtime)
                rt = rtime
            except:
                readtime = 'readtime'
                rt.append(readtime)

            try:
                designation = element.find_element(
                    By.XPATH, f"(//div[@class='playground-author-description f-13 text-primary'])[{x}]").text
                desig.append(designation)
                dg = desig
            except:
                designation = 'designation'
                dg.append(designation)

            try:
                authorname = element.find_element(
                    By.XPATH, f"(//div[@class='playground-author-name f-20 text-blue'])[{x}]").text
                aname.append(authorname)
                an = aname
            except:
                authorname = 'HariRam'
                an.append(authorname)

            try:
                blogimg = element.find_element(
                    By.XPATH, f"(//div[@class='playground-image']/img)[{x}]").get_attribute('src')
                imag.append(blogimg)
                img = imag
            except:
                blogimg = 'https://proshore.eu/wp-content/uploads/2022/05/kss-_hotjar-_feature-706x536.jpg'
                img.append(blogimg)

            # try:
            #     authorimg = element.find_element(
            #         By.XPATH, f"(//img[@class='avatar avatar-128 photo'])[{x}]").get_attribute('srcset')
            #     aimag.append({
            #         authorimg: authorimg
            #     })
            #     aimg = aimag
            # except:
            #     authorimg = 'https://secure.gravatar.com/avatar/e9299493040b2806468569ab4a3be1ce?s=128&d=mm&r=g'
            #     aimg.append(authorimg)


print(items, des, rt, dg, an, img)
print(len(items))

dataset_ar = pd.DataFrame(list(zip(items, des, rt,  an, dg, img)),
                          columns=['title', 'description', 'read-time',  'author-name', 'designation', 'blog-image'])

dataset_ar.to_csv('blogs.csv')
