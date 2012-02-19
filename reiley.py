#!/usr/bin/env python
# urllib allows us to encode the query string
# webbrowser allows us to open up pages in the webbrowser
import urllib, webbrowser

# The base url
dom="http://www.tv.com/search"

# Read in the tv show names from a text file
f=open("tv.txt")
data=f.readlines()
f.close()

# Loop through each show
for show in data:
    # Generate the url to search for each show
    # The show[:-1] eliminates the newline at the end of the string
    query=urllib.urlencode({"q":show[:-1]})
    url=dom+"?"+query

    # Open the url in the browser
    webbrowser.open(url)
