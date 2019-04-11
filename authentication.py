import os.path
from twython import Twython
from settings import *
from flipdotstreamer import FlipdotStreamer

CREDENTIALS_PATH = os.path.dirname(__file__) + "/data/credentials.txt"


def get_authenticated_streamer():
    try:
        with open("./data/credentials.txt", "r") as file:
            lines = file.readlines()
            FINAL_OAUTH_TOKEN = lines[0][:-1]
            FINAL_OAUTH_TOKEN_SECRET = lines[1]
            twitter = Twython(APP_KEY, APP_SECRET, FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)
            twitter.verify_credentials()
            return FlipdotStreamer(APP_KEY,APP_SECRET,FINAL_OAUTH_TOKEN,FINAL_OAUTH_TOKEN_SECRET)
    except:
        twitter = Twython(APP_KEY, APP_SECRET)
        auth = twitter.get_authentication_tokens()

        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

        print(auth['auth_url'])
        oauth_verifier = input('Enter your pin:')

        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        final_step = twitter.get_authorized_tokens(oauth_verifier)

        FINAL_OAUTH_TOKEN = final_step['oauth_token']
        FINAL_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

        twitter = Twython(APP_KEY, APP_SECRET, FINAL_OAUTH_TOKEN, FINAL_OAUTH_TOKEN_SECRET)
        twitter.verify_credentials()

        with open("./data/credentials.txt", "w") as file:
            file.write(FINAL_OAUTH_TOKEN + "\n" + FINAL_OAUTH_TOKEN_SECRET)

        return FlipdotStreamer(APP_KEY,APP_SECRET,FINAL_OAUTH_TOKEN,FINAL_OAUTH_TOKEN_SECRET)
