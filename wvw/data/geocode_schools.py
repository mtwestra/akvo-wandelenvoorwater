#!/usr/bin/python
import sqlite3
import sys
import urllib2
import time
import re

GEOCODEURL = "http://maps.googleapis.com/maps/api/geocode/xml?address=%s&region=nl&sensor=false" 

latlng_re=re.compile('<location>.*<lat>([-+]?[0-9]*\.?[0-9]+)</lat>.*<lng>([-+]?[0-9]*\.?[0-9]+)</lng>.*</location>',re.DOTALL)
loctype_re=re.compile('<location_type>(.+)</location_type>') 
try:
	conn = sqlite3.connect ('./WvW.sqlite')
except sqlite.Error, e:
     print "Error %d: %s" % (e.args[0], e.args[1])
     sys.exit (1)

cursor = conn.cursor ()
cursor.execute ("select id, ADRES, POSTCODE, PLAATS,GEOCODED from W4W_inschrijving where ACTIEF=1")

inschrijvingen = cursor.fetchall()
print "Number of inschrijvingen returned: %d" % len(inschrijvingen)

for inschrijving in inschrijvingen:
	
	A_id =inschrijving[0]
	A_adres =inschrijving[1]
	A_plaats = inschrijving[3]
	A_postcode=inschrijving[2]
	A_geocoded=inschrijving[4]

  
	if A_geocoded=='NONE':
		addr=A_adres+' '+A_postcode+' '+A_plaats
		addr=addr.encode('utf-8')
		addr=addr.replace('\t',' ')
		print "Geocoding address '%s'" % (addr)

		time.sleep(1)
		url = GEOCODEURL % (addr.replace(' ', '+'))

		mapcode = urllib2.urlopen(url).read()
     
		latlng_result=latlng_re.search(mapcode)
		loctype_result=loctype_re.search(mapcode)
  
		if latlng_result :
			longitude=latlng_result.group(1)
			latitude=latlng_result.group(2)
      
			print 'Result:' + longitude + ', ' + latitude
      
			if loctype_result :
				#print 'Quality: ' + loctype_result.group(1) 
				geocoded_result=loctype_result.group(1)
      
			else:
				print 'Quality: UNCLEAR'
				geocoded_result='UNCLEAR'
      
			#insert result in table scholen
			print 'inserting results in table'
			cursor.execute ("""update W4W_inschrijving set LONGITUDE = ?, LATITUDE = ?, GEOCODED = ? WHERE id = ?""",(longitude,latitude,geocoded_result,A_id))
			conn.commit ()
      
		else: 
			#print 'Geocoding failed'
			cursor.execute ("""update W4W_inschrijving set GEOCODED = ? where id = ?""",("FAILED",A_id))
			conn.commit ()
			
cursor.close()
conn.commit()
conn.close()
