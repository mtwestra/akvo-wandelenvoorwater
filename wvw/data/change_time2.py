import sqlite3
import sys
import urllib2
import time, datetime
import re

conn = sqlite3.connect('/Users/MarkTiele/1_Akvo/Software/Walking_for_Water/WvW/data/WvW.sqlite')

cursor = conn.cursor ()
cursor.execute ("SELECT id,DATUM_WANDELING FROM W4W_inschrijving")

rows = cursor.fetchall ()
print "Number of items returned: %d" % cursor.rowcount

for row in rows:
	
  A_id =row[0]
  A_datum_wandeling=row[1]
  
  print A_id, A_datum_wandeling
  if A_datum_wandeling=='':
    date_string_wandeling=''
  else:    
    temp_date_in=time.strptime(A_datum_wandeling, "%d-%m-%y")    
    date_string_wandeling=time.strftime("%Y-%m-%d",temp_date_in)
 
      
  #insert result in table scholen
  print 'inserting results in table'
  print date_string_wandeling
  cursor.execute ("""UPDATE W4W_inschrijving SET DATUM_WANDELING= ? WHERE id = ?""",(date_string_wandeling,A_id))
  
cursor.close ()
conn.commit ()
conn.close ()

################### end main programme ##########################

