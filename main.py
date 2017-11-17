#!/usr/bin/env python
from twython import Twython
import pytz
import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler


CONSUMER_KEY=os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET=os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET')


sched = BlockingScheduler()


@sched.scheduled_job('cron', minute=0)
def main():
    print "Scheduled job running..."

    # Generate the status that mcgrawtower will tweet
    tz = pytz.timezone("US/Eastern")
    dt = datetime.datetime.now(tz)
    hour = dt.hour % 12
    if hour == 0:
        hour = 12
    msg = "CHIME " * hour

    # Tweet the message out
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    try:
        result = twitter.update_status(status=msg)
        print result
    except Exception as e:
        print e
    finally:
        print "Done."

sched.start()
