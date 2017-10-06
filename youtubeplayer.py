from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from multiprocessing import Process

# # def playlist:
songsFile = open('songs.txt','r')
songs = songsFile.read().split('\n')
for song in songs:
	arg= song.split(' ')
	if '1' in arg:
		continue
	print('Now Playing: ' + song)
	driver.get('https://www.youtube.com/results?search_query=' + str(song))
	os.system('sleep 2')
	video = driver.find_element_by_id('video-title')
	video.click()
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ytp-time-duration")))
	duration = driver.find_element_by_class_name('ytp-time-duration')
	print(duration.text)
	next = input('press Enter for next song')
# class youtube:
# 	mainDriver = None
# 	def initDriver(self,url = 'https://www.youtube.com'):
# 		self.mainDriver = webdriver.Chrome()
# 		self.mainDriver.get(url)
# 	def playlist(self):
# 		songsFile = open('songs.txt', 'r')
# 		songs = songsFile.read().split('\n')
# 		for song in songs:
#
#
# print('Opening YouTube Shell')
# yt = youtube()
# playlist = Process(target = yt.playlist())
# while True:
# 	command = input('>>')
# 	if command == 'playlist':
# 		yt.initDriver()
# 		playlist.start()

