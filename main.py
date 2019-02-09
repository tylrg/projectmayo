import sys
from twython import Twython
import time
import json




# Secret Keys
apiKey = "qaiHFqWKyHuHWibbBOuJl3grj"
apiSecret = "mQ0w0YyeY5z5WkkDByI3TG9kI9OWzmmKGoe9A9BLEPeAhbm6Sj"
accessToken = "832293691888918533-6Mjald6xTQoGQw5UsLjyUNqkYbo1Ipo"
accessTokenSecret = "PKJJzwCU05e7UHgRtoRdVTYDRjZ48ksewf4arpQwlw18S"

#tweetStr="Hey, Jesse White!"
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#api.update_status(status=tweetStr)



class song:
    def __init__(self, user, name, recp, notes):
        self.user= user
        self.name = name
        self.recp = recp
        self.notes = notes
        self.played = False
    def play(self):
        print("Playing: "+ self.name)

tweet = api.get_mentions_timeline()

results = api.search(q="@project_mayo",count = 10);
all_tweets = results['statuses']
for tw in all_tweets:
    print(tw['text'])

    

#data = json.loads(tweet)
#print(tweet)

#location = content.find("u'text'")
#end = content.find("DONE")

#loop = True
#while loop:
#    print("loopdeloopandpull")
#    loop = False
#tweetStr="Hey, Jesse White!"
#api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#api.update_status(status=tweetStr)
