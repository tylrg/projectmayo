import sys
from twython import Twython
import time
import json
import os
import re
import dropbox
import subprocess

# Secret Keys
apiKey = ""
apiSecret = ""
accessToken = ""
accessTokenSecret = ""

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

tweet = api.get_mentions_timeline()
results = api.search(q="@project_mayo",count = 10);
all_tweets = results['statuses']
song_List = []
reading = True
content = ""
for tw in all_tweets:
    if reading:
        if tw['text'].find("NAME:")> 0:
            song_List.append(tw['text'])
    if tw['text'].find("DONE") < 0:
        reading = False

song_List.reverse()
for x in song_List:
    content = content + x

#everything is in content
songNameLoc = content.find("NAME:")+6
toLoc = content.find("TO")
songName = content[songNameLoc:toLoc-1]
print("Song Name: "+songName)
toLoc += 4
#print(content[toLoc])
recp = content[toLoc:content.find("!")]
print("To:" + recp)
end = content.find("DONE")
notes = content[content.find("!")+2:end]
print(notes)
#The song that is going to be played


#Name of file
songName = songName.replace(" ","_")

#conversion section for alda language
notes = notes.replace ("&lt;","<")
notes = notes.replace ("&gt;",">")


#printing songName and writing to alda
print("Playing:" + songName)
test = songName + ".txt"
test_object = open(test,"w")
test_object.write(notes)
test_object.close()
os.system("./alda play -f "+test)

#record system audio to a file


if len(songName)>0 :
    #upload to Dropbox
    dbx = dropbox.Dropbox("NViWwhEdVtAAAAAAAAAAWGmCiE9SH9BE097WfoRq4l8Hif21_OLbEb_F0TvYI4KC")
    file = open("/Users/tylergabriel/Desktop/CS/projectmayo/"+songName+".txt")
    dbx.files_upload(file.read(),"/"+songName+".txt")



    #reply to user
    tweetStr="Hey,"+recp+"! Here is a link to "+ songName+" , a song made just for you! https://www.dropbox.com/home/Apps/projectmayo?preview="+songName+".txt"
    api.update_status(status=tweetStr)
