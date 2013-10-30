import flickrapi

import datetime, time



flickr = flickrapi.FlickrAPI(c83487f5d94759be0bcbe9a480be02c8)

def get_data
	output = flickr.walk(min_upload_date=2013-01-01, bbox=-122.55,37.710,-122.35,37.81, accuracy=16, extras=geo, 2C, date_taken,format=json)
	

	write(output) to outputfile.whatever 

