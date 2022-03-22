#coding: utf-8
import os
os.system("pip install praw")
import praw
import urllib.request
client_Id = 'ENTER_CLIENT_ID'
client_Secret = "ENTER_CLIENT_SECRET"
usr='BOT_USERNAME'
pw='BOT_PASSWORD'
usr_agent='WEB_BROWSER_USER_AGENT'
subreddit='animemes'#Community name
url = []
url_title = []
url_parsed = []
path = os.getcwd()+"\\"
reddit = praw.Reddit(client_id = client_Id ,client_secret = client_Secret,username = usr,password = pw,user_agent = usr_agent)
for submission in reddit.subreddit(subreddit).hot(limit = 30):# 1 min = 60 pics api limit!
	url.append(submission.url)
	url_title.append(submission.title)
for title in url_title:
	url_parsed.append(''.join(s for s in title if s.isalnum()))
for index in range(len(url)):
	urllib.request.urlretrieve(url[index],path+url_parsed[index]+".jpg")
