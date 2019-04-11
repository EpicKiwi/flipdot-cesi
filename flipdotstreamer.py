from twython import TwythonStreamer
import re
import settings
import flipdotrender
import busconnector


class FlipdotStreamer(TwythonStreamer):

    hashtag_pattern = re.compile("^ *(.+) *#{} *$".format(settings.HASHTAG))

    def on_success(self, data):

        match_result = self.hashtag_pattern.match(data["text"])

        if match_result:
            print("Match    {} : {}".format(data["user"]["screen_name"], match_result.group(1)))
            res = flipdotrender.rendertext(match_result.group(1))
            busconnector.set_pixels(res)

    def on_error(self, status_code, data):
        print("ERROR", status_code, data)