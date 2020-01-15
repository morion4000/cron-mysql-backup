#!/usr/bin/python

import os
import time
import datetime
import sys

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

DB_USER = os.environ["DB_USER"]
DB_USER_PASSWORD = os.environ["DB_USER_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]
GDRIVE_ID = os.environ["GDRIVE_ID"]
DATE = time.strftime('%m%d%Y')

if len(sys.argv) < 2:
    print 'Must provide period'
    exit(1)

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

period = sys.argv[1];
filename = "%s_%s.sql" % (period, DATE)
FILE_PATH = "backups/%s" % filename

cmd = "mysqldump -u %s -p%s %s > %s" % (DB_USER, DB_USER_PASSWORD, DB_NAME, FILE_PATH)

os.system(cmd)

print "Created %s backup in %s" % (period, FILE_PATH)

file = drive.CreateFile({
    'title': filename,
    'parents': [{
        'isRoot': True,
        'kind': 'drive#parentReference',
        'id': GDRIVE_ID,
        'selfLink': '',
        'parentLink': ''
    }]
})
file.SetContentFile(FILE_PATH)
file.Upload()


print "Uploaded %s to Google Drive" % filename
