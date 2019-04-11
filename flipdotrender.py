import settings
from PIL import Image, ImageDraw, ImageFont
import datetime

font = ImageFont.truetype(settings.FONT_PATH,
                          size=settings.FONT_SIZE)

def rendertext(text):
    i = Image.new('RGB', (settings.FLIPDOT_WIDTH, settings.FLIPDOT_HEIGT), (0,0,0))
    d = ImageDraw.Draw(i)

    text_remaining = text
    linenum = 0
    while len(text_remaining) > 0:

        length = len(text_remaining)
        size = settings.FLIPDOT_WIDTH+1
        txt = text_remaining[:length]

        while size > settings.FLIPDOT_WIDTH:
            (size, h) = d.textsize(txt, font)

            if size > settings.FLIPDOT_WIDTH:
                length -= 1
                txt = text_remaining[:length]

        d.text(
            (0, ((settings.FLIPDOT_HEIGT/settings.FLIPDOT_LINENUMBER)*linenum)+linenum*settings.LINE_SKIP),
            txt,
            fill=(255, 255, 255),
            font=font)

        text_remaining = text_remaining[length:]
        linenum += 1

    now = datetime.datetime.now()
    i.save("./data/{}.png".format(now.strftime("%Y-%m-%d-%H-%M")))

    result = []
    for pixel in i.getdata():
        result += [((pixel[0]/255)+(pixel[1]/255)+(pixel[2]/255))/3]
    return result
