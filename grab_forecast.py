#!/usr/bin/env python
import requests

# Load station tags from stdin.
import sys

stns = []
locx = []
locy = []

def station_tags():
	elems = line.split()
	stns.append(elems[0]) #station name
	locx.append(float(elems[1]))
	locy.append(float(elems[2]))

def raw_data_load():
	tag_start = r.text.find(stn)
	if tag_start == -1:
		T = float('NaN')
	continue
	#tag_end = tag_start + 1720 #each text block is 1720 characters long

	T = float(r.text[tag_start+169:tag_start+172])
	print("%s\t%+6.2f\t%+6.2f\t%+3.0f"%(stn, locx[i], locy[i], T))

# Retrieve temperature data from online source.
# http://www.nws.noaa.gov/mdl/gfslamp/lavlamp.shtml
# Load raw data as HTML string.

for line in sys.stdin:
	station_tags()

r = requests.get('http://www.nws.noaa.gov/mdl/gfslamp/lavlamp.shtml')

#   We have a list of Illinois stations from the sites loaded previously.  We
#   need to load the data for each of those sites and store these data locally.
#   There are a lot of data included here, but we are only interested in one:
#   the current temperature, located at the index offset 169 and of length 2

#   (found by examination).
for (i, stn) in enumerate(stns):
	raw_data_load()


