'''
Author : Chittaranjan Kumar

This script will download the thumbnail of a YouTube video in highest resolution available (1080p) only.

'''

# pip install pyfiglet

import pyfiglet
ascii_banner = pyfiglet.figlet_format("YouTube Thumbnail Downloader")
print(ascii_banner)

#pip install wget

import wget
url=raw_input("Enter YouTube URL : ")
id = url.split("=",1)[1]
thumbnailurl= 'https://img.youtube.com/vi/'+id + '/maxresdefault.jpg'
print "Downloading Thumbnail..."
thumbnail = wget.download(thumbnailurl)
print "\n" + "Thumbnail Downloaded"
