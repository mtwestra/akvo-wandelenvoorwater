#!/usr/bin/python
import sqlite3
import sys
import urllib2
import time
import re
from django.utils.encoding import smart_str

try:
	conn = sqlite3.connect ('./WvW.sqlite')
except sqlite.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit (1)

cursor = conn.cursor ()
cursor.execute ("select id,STEUNPUNT_id,NAAM_SCHOOL,GEOCODED,latitude,longitude from W4W_inschrijving WHERE ACTIEF=1")

inschrijvingen = cursor.fetchall ()
#print "Number of inschrijvingen returned: %d" % len(inschrijvingen)

cursor.close ()
conn.commit ()
conn.close ()

now = time.time()
future = time.gmtime(now + 60)
y = future[0]
mo = future[1]
d = future[2]
h = future[3]
mi = future[4]
s = future[5]
iso8601 = '%04d-%02d-%02dT%02d:%02d:%02dZ' % (y,mo,d,h,mi,s)


KML_start="""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
 		<Style id="yellowpin"> 
      <IconStyle> 
        <Icon> 	
					<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> 
        </Icon> 
      </IconStyle> 
    </Style> 

		<Style id="greenpin"> 
      <IconStyle> 
        <Icon> 	
					<href>http://maps.google.com/mapfiles/kml/pushpin/grn-pushpin.png</href> 
        </Icon> 
      </IconStyle> 
    </Style> 
    
    	<Style id="purplepin"> 
      <IconStyle> 
        <Icon> 	
					<href>http://maps.google.com/mapfiles/kml/pushpin/purple-pushpin.png</href> 
        </Icon> 
      </IconStyle> 
    </Style> 
"""

KML_expires='<NetworkLinkControl> <expires>%s</expires> </NetworkLinkControl>' % iso8601

KML_end="""</Document></kml>"""

f = open('./schools.kml', 'w')
f.write(KML_start)
f.write(KML_expires)

for inschrijving in inschrijvingen:	
  A_id =inschrijving[0]
  A_steunp=inschrijving[1]
  
  A_naam=inschrijving[2]
  A_geocoded=inschrijving[3]
  A_lat=inschrijving[4]
  A_long=inschrijving[5]
  
  if (A_steunp==39): colorstring = '<styleUrl>#greenpin</styleUrl>'
  elif(A_steunp==24): colorstring = '<styleUrl>#purplepin</styleUrl>'
  elif(A_steunp==1): colorstring = '<styleUrl>#yellowpin</styleUrl>'
  else: colorstring = ''
  	
  if (A_geocoded!='NONE'):
    if (A_geocoded!='FAILED'):
    	if(A_geocoded!='RANGE_INTERPOLATED'):
    		# print A_naam +', ' + A_lat+', ' + A_long
    		KML_str='<Placemark><name>'+A_naam.encode('ascii','ignore')+'</name>'+colorstring+'<Point><coordinates>'+A_lat+','+A_long+',0</coordinates></Point></Placemark>\n'
    		# print KML_str
    		f.write(KML_str)
  
f.write(KML_end)
f.close   



################### end main programme ##########################

