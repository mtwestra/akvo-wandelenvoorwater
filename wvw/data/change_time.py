import sqlite3
import sys
import urllib2
import time, datetime
import re

conn = sqlite3.connect('/Users/MarkTiele/1_Akvo/Software/Walking_for_Water/WvW/data/WvW.sqlite')

cursor = conn.cursor ()
cursor.execute ("SELECT id,INVOER_DATUM,LAATSTE_WIJZIGING FROM W4W_inschrijving")

rows = cursor.fetchall ()
print "Number of items returned: %d" % cursor.rowcount

for row in rows:
	
  A_id =row[0]
  A_invoerdatum =row[1]
  A_last_update = row[2]
  
  print A_id, A_invoerdatum, A_last_update
      
  temp_date_in=time.strptime(A_invoerdatum, "%d-%m-%y")    
  temp_date_last=time.strptime(A_last_update, "%d-%m-%y")
  
  date_string_in=time.strftime("%Y-%m-%d %H:%M:%S",temp_date_in)
  date_string_last=time.strftime("%Y-%m-%d %H:%M:%S",temp_date_last)
  
      
  #insert result in table scholen
  print 'inserting results in table'
  print date_string_in, date_string_last
  cursor.execute ("""UPDATE W4W_inschrijving SET INVOER_DATUM = ?, LAATSTE_WIJZIGING = ? WHERE id = ?""",(date_string_in,date_string_last,A_id))
  
cursor.close ()
conn.commit ()
conn.close ()

################### end main programme ##########################

