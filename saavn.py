from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
songs = []
driver.get('https://www.saavn.com/s/playlist/tangiralasumanth389/Htnamus_2/rdGVXGDZ5aE_')
elements = driver.find_elements_by_class_name('song-wrap')
print('Finding songs ...')
for song in elements:
	element = song.find_element_by_class_name('main')
	name = element.find_element_by_class_name('title')
	songs.append(name.text)
songsFile = open('songs.txt', 'w')
for song in songs:
	songsFile.write(str(song) + '\n')
driver.close()
print('Stored in file')