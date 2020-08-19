from bs4 import BeautifulSoup
import urllib.request




content = urllib.request.urlopen("https://apod.nasa.gov/apod/archivepix.html").read()

BeautifulSoup(content, "lxml").findall("a")