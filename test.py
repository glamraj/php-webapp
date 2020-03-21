#!/usr/bin/env python
 
from selenium import webdriver
 
browser = webdriver.Firefox(executable_path='./geckodriver')

browser.get('http://www.google.com/')
