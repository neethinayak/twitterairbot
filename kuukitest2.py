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
    15: { "Compound" : "1_3-Butadiene", "Threshold" : -1 },
    16: { "Compound" : "t-2-Pentene", "Threshold" : -1 },
    17: { "Compound" : "1-Pentene", "Threshold" : -1 },
    18: { "Compound" : "c-2-Pentene", "Threshold" : -1 },
    19: { "Compound" : "2_2-Dimethylbutane", "Threshold" : -1 },
    20: { "Compound" : "2-Methylpentane", "Threshold" : -1 },
    21: { "Compound" : "Isoprene", "Threshold" : -1 },
    22: { "Compound" : "n-He-1ane", "Threshold" : -1 },
    23: { "Compound" : "Methylcyclopentane", "Threshold" : -1 },
    24: { "Compound" : "2_4-Dimethylpentane", "Threshold" : -1 },
    25: { "Compound" : "Benzene", "Threshold" : .4 },
    26: { "Compound" : "Cyclohe-1ane", "Threshold" : -1 },
    27: { "Compound" : "2-Methylhe-1ane", "Threshold" : -1 },
    28: { "Compound" : "2_3-Dimethylpentane", "Threshold" : -1 },
    29: { "Compound" : "3-Methylhe-1ane", "Threshold" : -1 },
    30: { "Compound" : "2_2_4-Trimethylpentane", "Threshold" : -1 },
    31: { "Compound" : "n-Heptane", "Threshold" : -1 },
    32: { "Compound" : "Methylcyclohe-1ane", "Threshold" : -1 },
    33: { "Compound" : "2_3_4-Trimethylpentane", "Threshold" : -1 },
    34: { "Compound" : "Toluene", "Threshold" : 1.65 },
    35: { "Compound" : "2-Methylheptane", "Threshold" : -1 },
    36: { "Compound" : "3-Methylheptane", "Threshold" : -1 },
    37: { "Compound" : "n-Octane", "Threshold" : -1 },
    38: { "Compound" : "Ethyl Benzene", "Threshold" : .6 },
    39: { "Compound" : "p-Xylene + m-Xylene", "Threshold" : -1 },
    40: { "Compound" : "Styrene", "Threshold" : -1 },
    41: { "Compound" : "o-Xylene", "Threshold" : .5 },
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
    "15": "1,3 Butadiene warning at %s! %s ppb. This may cause respiratory issues. For info:http://bit.ly/2ad4I9a",
    "25": "Benzene warning at %s. %s ppb. This is a carcinogenic compound. For info: http://bit.ly/29Q4sAu",
    "38": "Ethylbenzene warning at %s. %s ppb. May cause respiratory issues. For info: http://bit.ly/29JF2j4",
    "34": "Toluene level warning at %s. %s ppb. Toluene harms the nervous system. For info: http://bit.ly/29JFdL4",
    "40": "Styrene level warning at %s. %s ppb. Chronic exposure harms nervous system. For info: http://bit.ly/29Uzu8x",
    "41": "o-Xylene level warning at %s. %s ppb. May cause throat and gastro irritation. For info: http://bit.ly/2ac7oqn",
    "39": "Xylene levels warning at %s. %s ppb. May cause throat and gastro irritation. For info: http://bit.ly/2ac7oqn"
}

site_ids = {"48_201_0057" : "Galena Park", "48_039_1003": "Clute", "48_039_1004":
"Manvel Croix Park", "48_201_0026":
"Channelview",
         "48_039_1004" :
"Manvel Croix Park", "48_039_1012" :
"Freeport South Avenue I", 
"48_039_1016" :
"Lake Jackson",
         "48_071_0013" : "Smith Point Hawkins Camp", "48_071_1606" :
"UH Smith Point",
"48_157_0696": "UH Sugarland",
         "48_167_0004" : "Texas City Fire Station" , "48_167_0005" :
"Texas City Ball Park",
"48_167_0056" :
"Texas City 34th Street",
         "48_167_0571" :
"Clear Creek High School" , "48_167_0615" : "Texas City BP 31st Street Site 1", "48_167_0616" :
"Texas City BP Onsite (Site 2)",
"48_167_0621" :
"Texas City BP Logan Street (Site 3)",
         "48_167_0683" :
"Texas City 11th Street" , "48_167_0697" : "UH Coastal Center", 
"48_167_1034" :
"Galveston 99th Street",
         "48_167_5005" :
"Galveston Airport KGLS", 
"48_201_0024" :
"Houston Aldine", 
"48_201_0029" :
"Northwest Harris County",
"48_201_0036" :
"Jacinto Port",
         "48_201_0046" : "Houston North Wayside",
"48_201_0047" :
"Lang", 
"48_201_0051" :
"Houston Croquet",
         "48_201_0055" :
"Houston Bayland Park", "48_201_0058" :
"Baytown",
"48_201_0060"
: "Houston Kirkpatrick",
"48_201_0061" :
"Shore Acres",
         "48_201_0062" :
"Houston Monroe",
"48_201_0066" :
"Houston Westhollow", "48_201_0069" :
"Milby Park",
         "48_201_0071" : "Pasadena HL&P",
"48_201_0075" :
"Houston Texas Avenue", "48_201_0307" :
"Manchester/Central",
         "48_201_0416" :
"Park Place",
"48_201_0551" :
"Sheldon",
"48_201_0552" :
"Baytown Wetlands Center",
         "48_201_0553" :
"Crosby Library",
"48_201_0554" :
"West Houston",
"48_201_0556" :
"La Porte Sylvan Beach"
,
         "48_201_0557" :
"Mercer Arboretum" ,
"48_201_0558" :
"Tom Bass" ,
"48_201_0559" :
"Katy Park",
         "48_201_0560" :
"Atascocita",
"48_201_0561" :
"Meyer Park",
"48_201_0562" :
"Bunker Hill Village",
         "48_201_0563" :
"Huffman Wolf Road",
"48_201_0570" :
"Clear Brook High School",
"48_201_0572" :
"Clear Lake High School",
         "48_201_0617" :
"Wallisville Road",
"48_201_0669" :
"TPC FTIR South",
"48_201_0670" :
"TPC FTIR North",
         "48_201_0671" :
"Goodyear GC",
"48_201_0673" :
"Goodyear Houston Site 2", "48_201_0695" :
"UH Moody Tower",
         "48_201_0803" : "HRM 3 Haden Rd",
"48_201_1015" :
"Lynchburg Ferry",
"48_201_1017" :
"Baytown Garth",
         "48_201_1034" :
"Houston East",
"48_201_1035" :
"Clinton",
"48_201_1039" :
"Houston Deer Park 2",
         "48_201_1042" :
"Kingwood",
"48_201_1043" :
"La Porte Airport C243",
"48_201_1049" :
"Pasadena North",
         "48_201_1050" :
"Seabrook Friendship Park",
"48_201_1052" :
"Houston North Loop",
"48_201_1066" :
"Houston Southwest Freeway",
         "48_201_6000" :
"Cesar Chavez",
"48_291_0699" :
"UH West Liberty",
"48_339_0078" :
"Conroe Relocated",
         "48_339_0698" :
"UH WG Jones Forest",
"48_339_5006" :
"Conroe Airport KCXO",
"48_471_5012" :
"Huntsville KUTS" }
    

url = 'https://airbot.sugoisoft.com/readings'

headers = {'Authorization': 'Token ' + auth_token}
page = 1 
# messages.keys() returns the list of keys i.e. "15", "25", "38", "34".... and ",".join() will stringify as "15,25,.."
params = {'pollutant': ','.join(messages.keys()), 'site_id': ','.join(site_ids.keys()),
          'format': 'json', 'page':page}

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
        value = float(result['value'])
        site_id = str(result['location']['site_id'])
        try:
            site_name=site_ids[site_id]
        except KeyError:
            continue 

        properties = compounds[pollutant_num]
        compound = str(properties['Compound'])
        threshold = float(properties['Threshold'])

        # ignore compounds we aren't monitoring
        # With the pollutant(s) now being passed in params
        if threshold == -1:
            #print ("not monitoring %s..." % compound)
            continue

        tweet = ''
        if value > threshold:
            template = messages[str(pollutant_num)]
            tweet = (template % (site_name,value))
        else:
            #print ("%s levels are fine! :D" % compound)
            continue
           
        print (tweet)
        api.PostUpdate(tweet)

        
#TODO Exceptions for repeat tweets 
while True:
    params['page'] = page 
    response = requests.get(url, headers=headers, params=params)
    # response = requests.get(url, headers=headers, params=params)
    print (response)
    if not response:
        break
    data = response.json()
    print(data)
    process_response(data)
    page += 1 
    if data['next'] is None:
        break



