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


# Update the Twitter account
def tweet(msg):
    # Authorize the account
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # Update the status and store result in callback
    print twitter.update_status(status=msg)


@sched.scheduled_job('cron', minute=0)
def main():
    # Generate the status
    tz = pytz.timezone("US/Eastern")
    dt = datetime.datetime.now(tz)
    hour = dt.hour % 12
    if hour == 0:
        hour = 12
    msg = "CHIME " * hour
    tweet(msg)

sched.start()
