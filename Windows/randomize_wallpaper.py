# Author: Behnam Azizi
# Date: March 5, 2017
# Description: A Script to Update Wallpaper Based on Bing Image of the Day

import urllib
import re
import os
import ctypes

file_path, headers = urllib.urlretrieve("http://www.bing.com/")

with open(file_path, 'r') as f:
	image_url = 'http://www.bing.com' + re.findall(r'g_img\=\{url: \"([^\"]+)', f.read() )[0]
	image_path, headers = urllib.urlretrieve(image_url, "wallpaper.jpg")
	print(image_path, image_url)

	SPI_SETDESKWALLPAPER = 20 
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, os.getcwd() + "\\wallpaper.jpg" , 0)
