#coding: utf-8
import os,time
os.system("pip install praw opencv-python myigbot")
import praw,imghdr,cv2
import urllib.request
client_Id = 'CLIENT_ID'
client_Secret = "CLIENT_SECRET"
usr='BOT_USERNAME'
pw='BOT_PASSWORD'
usr_agent='USER_AGENT'
subreddit='goodanimemes'#animemes goodanimemes
url = []
url_title = []
url_parsed = []
file_list=[] # JPG File list
path = os.getcwd()+"\\"
counter=0
reddit = praw.Reddit(client_id = client_Id ,client_secret = client_Secret,username = usr,password = pw,user_agent = usr_agent)
for submission in reddit.subreddit(subreddit).hot(limit = 120):# 1 min = 60 pics api limit!
    url.append(submission.url)
    url_title.append(submission.title)
for title in url_title:
	url_parsed.append(''.join(s for s in title if s.isalnum()))
for index in range(len(url)):
    urllib.request.urlretrieve(url[index],path+url_parsed[index]+".jpg")
    time.sleep(1)
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".JPG") or file.endswith(".jpg"):
            file_list.append(os.path.join(file))
for name in file_list:
    file_type=imghdr.what(name)
    #print(name)
    new_file_name=str(counter)+'.jpg'
    #print(new_file_name)
    if os.path.exists(new_file_name):
        os.remove(new_file_name)
    os.rename(name,new_file_name)
    if file_type!='jpeg' and file_type!='png' or file_type=='none':
        #print(name + ' is not a JPEG! '+str(file_type)+' '+str(counter) )
        os.remove(new_file_name)
        counter+=1
        continue
    if file_type=='png':#convert png to jpg
        os.rename(new_file_name,'temp.jpg')
        image = cv2.imread('temp.jpg')
        cv2.imwrite(new_file_name, image, [int(cv2.IMWRITE_JPEG_QUALITY), 95]) #change 95 to 100 for max quality.
        os.remove('temp.jpg')
        counter+=1
    if file_type=='jpeg':
        counter+=1
        continue
