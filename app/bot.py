from instagrapi import Client
import random
import time
import logging
import os
import requests
from fake_useragent import UserAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Instantiating the Instagram client
cl = Client()

# Mimicking human behavior with random delays
cl.delay_range = [5, 15]  # Delay range to randomize requests further

# Random User-Agent for each request
ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

# Login (persist session using cookies)
def login():
    username = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")

    try:
        # Attempt to load session from file
        cl.load_settings("settings.json")
        if not cl.is_logged_in:
            cl.login(username, password)
            cl.dump_settings("settings.json")
        logging.info("Logged in successfully.")

    except Exception as e:
        logging.error(f"Login failed: {e}")

login()

def random_follow():
    users = ["public_user1", "public_user2", "public_user3"]
    user = random.choice(users)
    try:
        user_id = cl.user_id_from_username(user)
        cl.user_follow(user_id)
        logging.info(f"Followed: {user}")
    except Exception as e:
        logging.error(f"Failed to follow {user}: {e}")

def random_unfollow():
    try:
        following = cl.user_following(cl.user_id)
        if following:
            user_id = random.choice(list(following.keys()))
            cl.user_unfollow(user_id)
            logging.info(f"Unfollowed: {user_id}")
    except Exception as e:
        logging.error(f"Failed to unfollow: {e}")
