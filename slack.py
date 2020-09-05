import json, urllib.request    #urllib2 in python 2 is used as urllib.request in python 3
import datetime
import re

def slackMessage():
	text = "Message"
	payload = {
	"channel": "#testing",
	"username": "publisher",
	"text": text
	}    
	print (payload)
	request = urllib.request.Request("https://hooks.slack.com/services/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")     #created webhook from slack 
	request.add_header("Content-Type", "application/json")
	response = urllib.request.urlopen(request, data=json.dumps(payload).encode())   #.encode() is used to avoid type errors
	print(response)

slackMessage()