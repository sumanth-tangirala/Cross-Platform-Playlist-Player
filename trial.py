from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os
import signal
import sys

# pipeout, pipein = os.pipe()
# cpid = os.fork()
# if cpid != 0:
# 	os.close(pipein)
# 	pipeout = os.fdopen(pipeout)
# 	str = pipeout.read()
# 	print("Recieved string is: " + str)
# else:
# 	os.close(pipeout)
# 	pipein = os.fdopen(pipein,'w')
# 	print("Sending text")
# 	pipein.write("Hey there")
# 	exit(1)


# print ("The child will write text to a pipe and ")
# print ("the parent will read the text written by child...")
#
# # file descriptors r, w for reading and writing
# pipeout, pipein = os.pipe()
#
# processid = os.fork()
# if processid:
#    os.close(pipein)
#    pipeout = os.fdopen(pipeout)
#    print ("Parent reading")
#    str = pipeout.read()
#    print ("text =", str   )
#    sys.exit(0)
# else:
#    # This is the child process
#    os.close(pipeout)
#    pipein = os.fdopen(pipein, 'w')
#    print ("Child writing")
#    pipein.write("Text written by child...")
#    pipein.close()
#    print ("Child closing")
#    sys.exit(0)


from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.implicitly_wait(6)

driver.get("http://www.google.ca")

name=driver.find_element_by_xpath("""//*[@id="lst-ib"]""")

name.send_keys('how old is Obama')

name.send_keys(Keys.ENTER)
print("Searched for it")

name2=driver.find_element_by_class_name("_XWk")

print(name2)
print(name2.text)
print('Done printing it')
name2=driver.find_element_by_class_name("_uX kno-fb-ctx")

print(name2)
print(name2.text)
print('Done printing it')