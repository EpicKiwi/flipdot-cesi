import socketio
import settings
import time
import math

sio = socketio.Client()
sio.connect(settings.BUS_URL)


def set_pixels(pixels_array):

    i = 0
    for pixel in pixels_array:
        x = i % settings.FLIPDOT_WIDTH
        y = math.floor(i/settings.FLIPDOT_WIDTH)

        if pixel > settings.FONT_TOLERANCE:
            sio.emit("pixelYellow", {"X": x, "Y": y})
        else:
            sio.emit("pixelBlack", {"X": x, "Y": y})

        time.sleep(settings.BUS_SPEED)
        i += 1
