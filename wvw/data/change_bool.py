import sqlite3
import sys
import urllib2
import time, datetime
import re

conn = sqlite3.connect('/Users/MarkTiele/1_Akvo/Software/Walking_for_Water/WvW/data/WvW.sqlite')

cursor = conn.cursor ()
cursor.execute ("SELECT id,ACTIEF FROM W4W_inschrijving")

rows = cursor.fetchall ()
print "Number of items returned: %d" % cursor.rowcount

for row in rows:
	
  A_id =row[0]
  A_ACTIEF = row[1]
  
  print A_id,A_ACTIEF
      
  if A_ACTIEF==-1:
    A_ACTIEF=1
  else:
      A_ACTIEF=0
  
    
  #insert result in table scholen
  print 'inserting results in table'
  cursor.execute ("""UPDATE W4W_inschrijving SET ACTIEF = ? WHERE id = ?""",(A_ACTIEF,A_id))
  
cursor.close ()
conn.commit ()
conn.close ()

################### end main programme ##########################

