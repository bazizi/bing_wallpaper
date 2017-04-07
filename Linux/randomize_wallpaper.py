import urllib.request
import re
import os

file_path, headers = urllib.request.urlretrieve("http://www.bing.com/")

with open(file_path, 'r') as f:
	image_url = 'http://www.bing.com' + re.findall(r'g_img\=\{url: \"([^\"]+)', f.read() )[0]
	image_path, headers = urllib.request.urlretrieve(image_url)
	print( os.popen("gsettings set org.gnome.desktop.background picture-uri file://{path}".format(path=image_path) ).read())

