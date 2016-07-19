# -*- coding: utf-8 -*-

import requests
import twitter
import os

#import time  

AIRBOT_APP_KEY = os.environ['AIRBOT_APP_KEY']
AIRBOT_APP_SECRET = os.environ['AIRBOT_APP_SECRET']
AIRBOT_OAUTH_TOKEN = os.environ['AIRBOT_OAUTH_TOKEN']
AIRBOT_OAUTH_TOKEN_SECRET = os.environ['AIRBOT_OAUTH_TOKEN_SECRET']

api = twitter.Api(AIRBOT_APP_KEY, AIRBOT_APP_SECRET, AIRBOT_OAUTH_TOKEN, AIRBOT_OAUTH_TOKEN_SECRET)   

#TODO:
#add time frame of tweet
#don't tweet when levels are okay

auth_token = os.environ['SUGOISOFT_TOKEN']

#change to long term threshold
compounds = {
    2: { "Compound" : "Ethane", "Threshold" : -1 },
    3: { "Compound" : "Ethylene", "Threshold" : -1 },
    4: { "Compound" : "Propane", "Threshold" : -1 },
    5: { "Compound" : "Propylene", "Threshold" : -1 },
    6: { "Compound" : "Isobutane", "Threshold" : -1 },
    7: { "Compound" : "n-Butane", "Threshold" : -1 },
    8: { "Compound" : "Acetylene", "Threshold" : -1 },
    9: { "Compound" : "t-2-Butene", "Threshold" : -1 },
    10: { "Compound" : "1-Butene", "Threshold" : -1 },
    11: { "Compound" : "c-2-Butene", "Threshold" : -1 },
    12: { "Compound" : "Cyclopentane", "Threshold" : -1 },
    13: { "Compound" : "Isopentane", "Threshold" : -1 },
    14: { "Compound" : "n-Pentane", "Threshold" : -1 },
    15: { "Compound" : "1_3-Butadiene", "Threshold" : 9.1 },
    16: { "Compound" : "t-2-Pentene", "Threshold" : -1 },
    17: { "Compound" : "1-Pentene", "Threshold" : -1 },
    18: { "Compound" : "c-2-Pentene", "Threshold" : -1 },
    19: { "Compound" : "2_2-Dimethylbutane", "Threshold" : -1 },
    20: { "Compound" : "2-Methylpentane", "Threshold" : -1 },
    21: { "Compound" : "Isoprene", "Threshold" : -1 },
    22: { "Compound" : "n-He-1ane", "Threshold" : -1 },
    23: { "Compound" : "Methylcyclopentane", "Threshold" : -1 },
    24: { "Compound" : "2_4-Dimethylpentane", "Threshold" : -1 },
    25: { "Compound" : "Benzene", "Threshold" : 1.4 },
    26: { "Compound" : "Cyclohe-1ane", "Threshold" : -1 },
    27: { "Compound" : "2-Methylhe-1ane", "Threshold" : -1 },
    28: { "Compound" : "2_3-Dimethylpentane", "Threshold" : -1 },
    29: { "Compound" : "3-Methylhe-1ane", "Threshold" : -1 },
    30: { "Compound" : "2_2_4-Trimethylpentane", "Threshold" : -1 },
    31: { "Compound" : "n-Heptane", "Threshold" : -1 },
    32: { "Compound" : "Methylcyclohe-1ane", "Threshold" : -1 },
    33: { "Compound" : "2_3_4-Trimethylpentane", "Threshold" : -1 },
    34: { "Compound" : "Toluene", "Threshold" : 1100 },
    35: { "Compound" : "2-Methylheptane", "Threshold" : -1 },
    36: { "Compound" : "3-Methylheptane", "Threshold" : -1 },
    37: { "Compound" : "n-Octane", "Threshold" : -1 },
    38: { "Compound" : "Ethyl Benzene", "Threshold" : 450 },
    39: { "Compound" : "p-Xylene + m-Xylene", "Threshold" : 140 },
    40: { "Compound" : "Styrene", "Threshold" : 110},
    41: { "Compound" : "o-Xylene", "Threshold" : 140 },
    42: { "Compound" : "n-Nonane", "Threshold" : -1 },
    43: { "Compound" : "Isopropyl Benzene - Cumene", "Threshold" : -1 },
    44: { "Compound" : "n-Propylbenzene", "Threshold" : -1 },
    45: { "Compound" : "1_3_5-Trimethylbenzene", "Threshold" : -1 },
    46: { "Compound" : "1_2_4-Trimethylbenzene", "Threshold" : -1 },
    47: { "Compound" : "n-Decane", "Threshold" : -1 },
    48: { "Compound" : "1_2_3-Trimethylbenzene", "Threshold" : -1 },
    49: { "Compound" : "2-Methyl-2-Butene", "Threshold" : -1 }
}

#Tweets check characters  
messages = {
    "15": "1,3 Butadiene levels are high at %s! This may cause respiratory issues. For info:http://bit.ly/2ac7oqn",
    "25": "Benzene levels at %s are too high. This is a carcinogenic compound. For info: http://bit.ly/29Q4sAu",
    "38": "Ethylbenzene levels are high today at %s. May cause respiratory issues. For info: http://bit.ly/29JF2j4",
    "34": "Toluene levels over threshold at %s. Toluene harms the nervous system. For info: http://bit.ly/29JFdL4",
    "40": "Styrene levels over threshold at %s. Chronic exposure harms nervous system. For info: http://bit.ly/29Uzu8x",
    "41": "o-Xylene levels over threshold at %s. May cause throat and gastro irritation. For info: http://bit.ly/2ac7oqn",
    "39": "Xylene levels over threshold at %s. May cause throat and gastro irritation. For info: http://bit.ly/2ac7oqn"
}

url = 'https://airbot.sugoisoft.com/thresholds'

headers = {'Authorization': 'Token ' + auth_token}

# messages.keys() returns the list of keys i.e. "15", "25", "38", "34".... and ",".join() will stringify as "15,25,.."
params = {'pollutant': ','.join(messages.keys()), 'site_id': '48_201_0026,48_355_0041',  # Specify the site ids you want to monitor here
          'format': 'json'}

def process_response(data):
    """
    Takes json data from airbot and prints out the message that will be tweeted in v3
    :param data:  json from airbot
    :return:
    """
    results = data['results']

    for result in results:
        #print (result)
        pollutant_num = result['pollutant']
        total = float(result['sum'])
        # site_id = str(result['site_id'])  #  Unused
        # site_name= sites[site_id]         #  Unused

        properties = compounds[pollutant_num]
        compound = str(properties['Compound'])
        threshold = float(properties['Threshold'])

        # ignore compounds we aren't monitoring
        # With the pollutant(s) now being passed in params
        if threshold == -1:
            # print ("not monitoring %s..." % compound)
            continue

        tweet = ''
        if total > threshold:
            template = messages[str(pollutant_num)]
            tweet = (template % total)
        else:
            continue
            #tweet = ("%s levels are fine! :D" % compound)

        print (tweet)
        api.PostUpdate(tweet)

        

while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    #print(data)
    tweet = process_response(data)

    url = data['next']
    if url is None:
        break



