#!/bin/bash
####################################
#
# updating kml file of schools in Wandelen voor Water. Only active schools are included, and those that have a geocode.
#
####################################

echo updating geocoding database

# update geocoding database
python geocode_schools.py

# Print end status message.

echo generating new kml file
python make_kml.py

echo copying kml file to right location
mv ./schools.kml /home/mtwestra/public_html/html/schools7.kml