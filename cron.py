#!/usr/bin/python

import os

from crontab import CronTab

system_cron = CronTab()

backup_cmd = "/usr/bin/python backup.py"
clean_cmd = "/usr/bin/python clean.py"

# daily kept for one week
# weekly kept for 4 weeks
# monthly kept for 3 months
# quarterly kept for ever

system_cron.new(command="%s daily" % backup_cmd).setall('0 0 * * *') # daily
system_cron.new(command="%s weekly" % backup_cmd).setall('0 0 * * SUN') # weekly
system_cron.new(command="%s monthly" % backup_cmd).setall('0 0 1 * *') # monthly
system_cron.new(command="%s quarterly" % backup_cmd).setall('0 0 1 JAN,APR,JUL,OCT *') #quarterly

system_cron.new(command=clean_cmd).setall('0 0 * * SUN') # weekly

system_cron.write()
