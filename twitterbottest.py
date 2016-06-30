
#import tweepy 
#import time  
#APP_KEY = ""  
#APP_SECRET = ""  
#OAUTH_TOKEN = ""  
#OAUTH_TOKEN_SECRET = ""
#twitter = Twython (APP_KEY, APP_SECRET, PAUTH_TOKEN, OAUTH_TOKEN_SECRET)   
#api.update_status(tweet)   

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
15: { "Compound" : "1_3-Butadiene", "Threshold" : 1700 },
16: { "Compound" : "t-2-Pentene", "Threshold" : -1 },
17: { "Compound" : "1-Pentene", "Threshold" : -1 },
18: { "Compound" : "c-2-Pentene", "Threshold" : -1 },
19: { "Compound" : "2_2-Dimethylbutane", "Threshold" : -1 },
20: { "Compound" : "2-Methylpentane", "Threshold" : -1 },
21: { "Compound" : "Isoprene", "Threshold" : -1 },
22: { "Compound" : "n-He-1ane", "Threshold" : -1 },
23: { "Compound" : "Methylcyclopentane", "Threshold" : -1 },
24: { "Compound" : "2_4-Dimethylpentane", "Threshold" : -1 },
25: { "Compound" : "Benzene", "Threshold" : 180 },
26: { "Compound" : "Cyclohe-1ane", "Threshold" : -1 },
27: { "Compound" : "2-Methylhe-1ane", "Threshold" : -1 },
28: { "Compound" : "2_3-Dimethylpentane", "Threshold" : -1 },
29: { "Compound" : "3-Methylhe-1ane", "Threshold" : -1 },
30: { "Compound" : "2_2_4-Trimethylpentane", "Threshold" : -1 },
31: { "Compound" : "n-Heptane", "Threshold" : -1 },
32: { "Compound" : "Methylcyclohe-1ane", "Threshold" : -1 },
33: { "Compound" : "2_3_4-Trimethylpentane", "Threshold" : -1 },
34: { "Compound" : "Toluene", "Threshold" : 4000 },
35: { "Compound" : "2-Methylheptane", "Threshold" : -1 },
36: { "Compound" : "3-Methylheptane", "Threshold" : -1 },
37: { "Compound" : "n-Octane", "Threshold" : -1 },
38: { "Compound" : "Ethyl Benzene", "Threshold" : 20000 },
39: { "Compound" : "p-Xylene + m-Xylene", "Threshold" : -1 },
40: { "Compound" : "Styrene", "Threshold" : 5100 },
41: { "Compound" : "o-Xylene", "Threshold" : -1 },
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
	
while continuing:
	
	r = requests.get(url)
	
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
		
		properties = compounds[pollutant_num]
		
		compound = str(properties['Compound'])
		threshold = float(properties['Threshold'])
	
		#ignore compounds we aren't monitoring
		if threshold == -1:
			print ("not monitoring %s..." % compound)
			continue
	
		if total > threshold:
			print ("%s levels today have exceeded the recommended threshold. Hide ya kids hide ya wife." % compound)
		else:
			print ("%s levels are fine! :D" % compound)
		
		
exit()

#Benzene check compound number 
#	for line in buff[:]:
#		if "pollutant":25.sum>0: 
#			print ("Benzene levels today have exceeded the recommended threshold. Take the necessary safety precautions")
#			twitter.update_status(status=line)
#			
#		else:
#			print ("Benzene levels did not exceed thresholds today")
#
#Ethylbenzene
#	for line in buff [:]:
#		if "pollutant":38.sum> 20000 
#		print ("Ethylbenzene levels have exceeded the recommended threshold. Take the necesary safety precautions")
#		twitter.update_status(status=line) 
#	
#	else:
#		print ("Ethylbenzene levels did not exceed thresholds today") 
#		
##Toluene 	
#	for line in buff [:]:
#		if "pollutant":34.sum> 4000
#		print ("Toluene levels have exceeded the recommended threshold. Take the necesary safety precautions")
#		twitter.update_status(status=line) 
#	
#	else:
#		print ("Toluene levels did not exceed thresholds today") 
#
##1,3 Butadine  	
#	for line in buff [:]:
#		if "pollutant":15.sum> 1700
#		print ("1, 3 Butadine levels have exceeded the recommended threshold. Take the necesary safety precautions")
#		twitter.update_status(status=line) 
#	
#	else:
#		print ("1, 3 Butadine levels did not exceed thresholds today")
#
##Styrene 
#	for line in buff [:]:
#	if "pollutant":40.sum> 5100 
#	print ("Styrene levels today have exceeded the recommended threshold. Take the necessary safety precautions") 
#	twitter.update_status(status=line) 
#	
#	else: 
#		print("Styrene levels did not exceed thresholds today") 
#
