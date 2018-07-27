## Strava Gpx Downloader

Strava allows only premium users to download gpx files. This Python script allow you to bypass that limitation and download gpx of other riders/runners without a premium account.

The script has both CLI and GUI. There is also a single file pre-builded version for Windows. 


### REQUIREMENTS

* Python 3.6
* requests 2.5.3
* PyQt5 5.11.2
* gpxpy 1.3.3

The list of dependencies are listed in `./requirements.txt`.  
To install automatically all the dependencies execute `pip3 install -r requirements.txt`

### CLI

```
>> python3 gpxDownloader.py
Usage: gpxDownloader.py [options]

Options:
  -h, --help            show this help message and exit
  -a ACTIVITY_ID, --activity=ACTIVITY_ID
                        Id of Strava activity
  -o OUTPUT_FILENAME, --output=OUTPUT_FILENAME
                        Name of the output file

```

If you want download the activity *0123456789* in the file *mytrack.gpx* using the CLI, just type:   

`python3 gpxDownloader.py -a 0123456789 -o mytrack.gpx` 

### GUI

If you want use the GUI just type:   

`python3 main.py`

### Pre-Builded Windows Binary 

For *Windows* users, you can download a pre-builded version [here](./dist/main.exe)
