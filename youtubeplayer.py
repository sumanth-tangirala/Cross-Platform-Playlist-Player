from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import requests
from bs4 import BeautifulSoup
import time
import signal
NEXT = 1
PREV = -1
CURR = 0
def TimeParse(duration):
	time = {'hrs':0,'mins':0,'secs':0}
	duration = duration.split(' ')[-1]
	duration = duration.split(':')
	if len(duration) == 3:
		time['hrs'] = int(duration[0])
		time['mins'] = int(duration[1])
		time['secs'] = int(duration[2][:-1])
	else:
		time['mins'] = int(duration[0])
		time['secs'] = int(duration[1][:-1])
	return time



class youtube:
	def __init__(self,songs,driver,namein,nameout):
		self.current = 0
		self.cpid = 0
		self.pid = os.getpid()
		self.currentno = 0
		self.namein = namein
		self.nameout = nameout
		self.songs = songs
		self.driver = driver

	def pltPlay(self):
		self.cpid = os.fork()
		if self.cpid == 0:  # CHILD Process that handles the playlist playing
			os.close(self.nameout)

			while True:
				song = self.SongChooser()
				print("Song name written to the pipe")
				songAndNum = song + '|||' + str(self.currentno)
				os.write(self.namein,songAndNum)
				if song != -1:
					waitTime = self.play(song)
					a = time.sleep(waitTime)
				else:
					break
			print('All songs in the playlist are done')
			exit(2)

		else: #Parent process that has to do some stuff yet
			print("I'm inside parent")
			os.close(self.namein)
			songname = self.nameout
			print("I'm going to read")
			print(os.read(songname,100))
			print("Song name read")
			# self.current = songAndNum.split('|||')[0]
			# self.currentno = int(songAndNum.split('|||')[1])
			# print('Song being played is: '+ self.current)
			# print('Song number is: ' + self.currentno)


	def SongChooser(self,skip = False, req = NEXT):
		if skip == False and req == NEXT :
			self.current = self.songs[self.currentno + 1]
			self.currentno += 1
			return self.current
		else:
			a = 1


	def play(self,song):
		code = requests.get('https://www.youtube.com/results?search_query=' + str(song))
		text = code.text
		soup = BeautifulSoup(text, 'html.parser')
		duration = soup.find(class_ = 'accessible-description')
		duration = duration.text
		dur = TimeParse(duration)
		waitTime = dur[ 'hrs' ] * 3600 + dur[ 'mins' ] * 60 + dur[ 'secs' ] + 3
		link = soup.find(
			class_ = 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ')
		link = link.get('href')
		link = 'https://www.youtube.com' + link
		self.driver.get(link)
		return waitTime

	def skip(self):
		if self.cpid == 0:
			a = 1

def main():
	songsFile = open('/Users/Htnamus/All Stuff/Programming Stuff/Saavn2Spotify/songs.txt', 'r')
	songs = songsFile.read().split('2\n')[ 1 ].split('\n')# List of all the names of the songs
	driver = webdriver.Chrome()
	nameout, namein = os.pipe()

	def handler( sig, frame ):
		print("Signal Recieved")

	signal.signal(signal.SIGUSR1, handler)
	print('Opening YouTube Shell')
	yt = youtube(songs,driver,namein, nameout)
	while True:
		yt.pltPlay()
		break



	try:
		driver.close()
	except:
		pass


main()
