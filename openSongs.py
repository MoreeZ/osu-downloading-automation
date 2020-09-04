import time
import json
import webbrowser
import os
import configparser

# Load config from config file
config = configparser.ConfigParser()
config.read('config.ini')

offsetLength = config['openSongs']['offsetLength']

# Check if data file exists
if not os.path.isfile('jsonData.json'):
    print("You must first run option 1 to create a data file!")
    quit()
else:
    jsonFile = open('jsonData.json', 'r', encoding='utf-8')
    
data = json.loads(jsonFile.read())
offset = 0
maximumOffset = round(len(data) / int(offsetLength))
print('==================================================')
print('Your data file has ' + str(len(data)) + ' songs.')
print('Each offset: ' + offsetLength + ' songs')
print('Maximum allowed offset number: ' + str(maximumOffset))
print('Start at offset: 1')
print('REMEMBER: You will need to change your public IP between each offset in order to avoid "Too Many Requests" error.')
print('==================================================')

# Run the main script
while True:
    userInput = input('offset number: ')
    try:
        offset = int(userInput)
    except ValueError:
        print("That's not an int!")
    finally:
        if offset <= maximumOffset:
            rangeOfData = [ beatmap for beatmap in data if data.index(beatmap) > (offset - 1) * int(offsetLength) and data.index(beatmap) <= offset * int(offsetLength) ]
            print([data.index(beatmap) for beatmap in rangeOfData][0], [data.index(beatmap) for beatmap in rangeOfData][-1])

            for beatmap in rangeOfData:
                webbrowser.open_new_tab("https://osu.ppy.sh/beatmapsets/" + str(beatmap['beatmapset_id']))
                time.sleep(0.1)
        else:
            print('If you want to go above your maximum offset number: ' + str(maximumOffset) + ' you will need to increase "offsetQuantity" in config.ini file and download the data file again.')
