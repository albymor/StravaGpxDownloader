from optparse import OptionParser
import gpxpy
import gpxpy.gpx
import requests
import json
import sys

STRAVA_STREAM_URL = 'http://www.strava.com/stream/'
DATA={'streams[]': ['latlng', 'altitude', 'time']}


def downloader(activityID, filename):

	r = requests.get(STRAVA_STREAM_URL + activityID, params=DATA)

	json_track = json.loads(r.text)

	gpx = gpxpy.gpx.GPX()

	# Create first track in our GPX:
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx.tracks.append(gpx_track)

	# Create first segment in our GPX track:
	gpx_segment = gpxpy.gpx.GPXTrackSegment()
	gpx_track.segments.append(gpx_segment)

	for latlng, altitude in list(zip(json_track['latlng'], json_track['altitude'])):
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(
			latlng[0], latlng[1], elevation=altitude))

	filename = filename if '.gpx' in filename else filename + '.gpx'

	with open(filename, 'w') as fw:
		fw.write(gpx.to_xml())

	fw.close()


def main():

	parser = OptionParser()

	parser.add_option("-a", "--activity", dest="activity_id", help="Id of Strava activity", default=None)

	parser.add_option("-o", "--output", dest="output_filename", help="Name of the output file", default="stravaOut.gpx")

	(options, args) = parser.parse_args(sys.argv)

	if options.activity_id == None:
		parser.print_help()
		sys.exit(1)

	downloader(options.activity_id, options.output_filename)

	sys.exit(0)
	

if __name__ == '__main__':
	main()
