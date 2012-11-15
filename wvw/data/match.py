import sqlite3
import sys
import urllib2
import time
import re

conn = sqlite3.connect('/Users/MarkTiele/1_Akvo/Software/Walking_for_Water/WvW/data/WvW.sqlite')

cursor = conn.cursor ()
cursor.execute ("SELECT id,inschrijving,gematched FROM scholen_wvw_2011")

rows = cursor.fetchall ()
print "Number of items returned: %d" % cursor.rowcount

for row in rows:
	
  A_id =row[0]
  A_inschrijving =row[1]
  A_gematched = row[2]
  
  print A_id, A_inschrijving, A_gematched
      
  #insert result in table scholen
  print 'inserting results in table'
  cursor.execute ("""UPDATE W4W_inschrijving SET BRIN_NUMMER = ? WHERE id = ?""",(A_gematched,A_inschrijving))
  
cursor.close ()
conn.commit ()
conn.close ()

################### end main programme ##########################

