import sys
from twython import Twython
import time




# Secret Keys
apiKey = "qaiHFqWKyHuHWibbBOuJl3grj"
apiSecret = "mQ0w0YyeY5z5WkkDByI3TG9kI9OWzmmKGoe9A9BLEPeAhbm6Sj"
accessToken = "832293691888918533-6Mjald6xTQoGQw5UsLjyUNqkYbo1Ipo"
accessTokenSecret = "PKJJzwCU05e7UHgRtoRdVTYDRjZ48ksewf4arpQwlw18S"




class song:
    def __init__(name, tempo, notes, key, user):
        self.name = name
        self.age = age
        self.tempo = tempo
        self.notes = notes
        self.key = key
        self.user = user
        self.played = False
    def play(self):
        print("Playing: "+ self.name)

bool=l
while




















tweetStr="Hey, Jesse White!"
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)
