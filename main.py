import authentication
import busconnector
import flipdotrender
import settings

#stream = authentication.get_authenticated_streamer()
#print("Started watcher on hashtag #{}".format(settings.HASHTAG))
#stream.statuses.filter(track='#{}'.format(settings.HASHTAG))

res = flipdotrender.rendertext("Les vulcanologues ont tous les oreilles pointues." )
busconnector.set_pixels(res)