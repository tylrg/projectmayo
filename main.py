import sys
from twython import Twython
import time




# Secret Keys
apiKey = "qaiHFqWKyHuHWibbBOuJl3grj"
apiSecret = "mQ0w0YyeY5z5WkkDByI3TG9kI9OWzmmKGoe9A9BLEPeAhbm6Sj"
accessToken = "832293691888918533-6Mjald6xTQoGQw5UsLjyUNqkYbo1Ipo"
accessTokenSecret = "PKJJzwCU05e7UHgRtoRdVTYDRjZ48ksewf4arpQwlw18S"
























tweetStr="Hey, Jesse White!"
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)
