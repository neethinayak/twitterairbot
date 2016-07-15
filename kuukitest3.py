import twitter 
#import time  

from local_settings import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
api = twitter.Api(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)   
#api.PostUpdate("hello, world!")
#heroku,cron job, 
#add time frame of tweet
#don't tweet when levels are okay

import requests

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

continuing = True
url = 'https://airbot.sugoisoft.com/thresholds/?format=json'
headers={'Authorization': 'access_token myToken'}

#Tweets check characters  
messages= {"15": "1,3 Butadiene has high levels today at %s! This compound causes respiratory issues. For info:https://www3.epa.gov/airtoxics/hlthef/xylenes.html",
           "25": "Benzene levels at %s are over threshold. This is a cancer causing compound that is undesirable in the air. For info: https://www3.epa.gov/airtoxics/hlthef/benzene.html",
           "38": "Ethylbenzene is known to cause respiratory irritation. Levels are high today at %s. For info: https://www3.epa.gov/airtoxics/hlthef/ethylben.html",
           "34": "Toluene levels are over threshold at %s. This compound damages to the nervous system. For info: https://www3.epa.gov/airtoxics/hlthef/toluene.html",
           "40": "Styrene levels are over threshold at %s. Chronic exposure damages the central nervous system. For info: https://www3.epa.gov/airtoxics/hlthef/styrene.html",
           "41": "o-Xylene levels are over threshold at %s. The compound causes throat and gastro irritation. For info: https://www3.epa.gov/airtoxics/hlthef/xylenes.html",
           "39": "Xylene levels are over threshold at %s. The compound causes throat and gastro irritation. For info: https://www3.epa.gov/airtoxics/hlthef/xylenes.html"}
           
tweet = ""

while continuing:
	
	r = requests.get(url, headers=headers)
	print(r)
	
	#TODO check if r is bad??
	
	results = r.json()['results']
	next = r.json()['next']
	
	if not next:
		continuing = false
	else:
		url = next
	
	for i in range(len(results)):
		pollutant_num = results[i]['pollutant']
		total = float(results[i]['sum'])
		site_id = str(result['site_id'])
		site_name= sites[site_id]
		properties = compounds[pollutant_num]
		
		compound = str(properties['Compound'])
		threshold = float(properties['Threshold'])
	
		#ignore compounds we aren't monitoring
		if threshold == -1:
			print ("not monitoring %s..." % compound)
			continue
	
		if total > threshold:
			template = messages [str(pollutant_num)]
			tweet = (template % total) 
		else:
			tweet = ("%s levels are fine! :D" % compound)


if tweet:
        print (tweet)
        #api.PostUpdate(tweet)
else:
        print ("couldn't construct a tweet")
