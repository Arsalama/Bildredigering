from PIL import Image, ImageDraw

WHITE = (255,255, 255)
BLUE = (24, 41, 88)

im = Image.new("RGB", (180, 110), WHITE)

imd = ImageDraw.Draw(im)

imd.rectangle([(50, 0), (80, 110)], BLUE)
imd.rectangle([(0, 40), (180, 70)], BLUE)


im.save("flag.png")
