#!/usr/bin/env python3
"""
Tweets a explanation of an stdlib C function every set amount of minutes
"""
import json
import tweepy
import random
import time

with open("config.json", "r", encoding="utf-8") as read_file:
    auth_data = json.load(read_file)

client = tweepy.Client(consumer_key=auth_data["API_KEY"],
                        consumer_secret=auth_data["API_KEY_SECRET"],
                        access_token=auth_data["ACCESS_TOKEN"],
                        access_token_secret=auth_data["ACCESS_TOKEN_SECRET"])

# Cooldown time between tweets in minutes
TIME_INTERVAL = 30

# Opens JSON file with C functions (taken from https://www.ibm.com/docs/en/i/7.1?topic=extensions-standard-c-library-functions-table-by-name and formatted into JSON)
with open("functions.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)

"""
Takes an object from the JSON as argument, returns it formatted ready for tweeting.
"""
def format_json(obj):
    prot = obj["function_prototype"]
    sysinc = obj["system_include_file"]
    desc = obj["description"]

    return f"{prot} from {sysinc}\n\n{desc}"

"""
Tweets the argument passed
"""
def tweet(data):
    client.create_tweet(text=data)

"""
Main loop

Tweets a random C function every set amount of minutes
"""
while True:
    # Randomly select a function from the JSON
    random_function = random.choice(data)
    # Format the function
    formatted_function = format_json(random_function)
    # Tweet the function
    tweet(formatted_function)
    # Wait for the set amount of minutes
    time.sleep(TIME_INTERVAL * 60)

tweet()
