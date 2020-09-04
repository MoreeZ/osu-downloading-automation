import requests
import json
from tqdm import tqdm
import time
import configparser
import os

# Load config from config file
config = configparser.ConfigParser()
config.read('config.ini')

offsetQuantity = config['getData']['offsetQuantity']
requestDelay = config['getData']['requestDelay']
link = config['osusearch']['link'].replace('https://osusearch.com/search/', 'https://osusearch.com/query/')

allData = []
for i in tqdm (range (int(offsetQuantity)), desc="Fetching beatmaps..."): 
    response = requests.get(link + "&offset=" + str(i)).json()
    allData = allData + response['beatmaps']
    time.sleep(float(requestDelay))
    
# Save the data into a json file
jsonFile = open('jsonData.json', 'w+', encoding='utf-8')
jsonFile.write(json.dumps(allData))

# Ask the user if they want to proceed to step 2
answer = ""
while not(answer == "y" or answer == "n"):
    answer = input("Proceed to part 2? [Y/N]").lower()
    if answer == "y":
        os.system('python openSongs.py')
        quit()
    if answer == "n":
        quit()
