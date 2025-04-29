# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from app.bot import random_follow, random_unfollow
import random
import logging

def start_scheduler():
    scheduler = BackgroundScheduler()

    follow_interval = random.randint(1800, 3600)  # 30 to 60 minutes
    unfollow_interval = random.randint(3600, 5400)  # 60 to 90 minutes

    scheduler.add_job(random_follow, 'interval', seconds=follow_interval, id='follow_job')
    scheduler.add_job(random_unfollow, 'interval', seconds=unfollow_interval, id='unfollow_job')

    scheduler.start()
    logging.info("Scheduler started with stealthy randomized intervals.")
