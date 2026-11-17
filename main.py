from PIL import Image, ImageDraw

BLUE = (255,255, 255)
WHITE = (24, 41, 88)

im = Image.new("RGB", (160, 100), BLUE)

imd = ImageDraw.Draw(im)

imd.rectangle([(60, 0), (80, 100)], WHITE)
imd.rectangle([(0, 40), (160, 60)], WHITE)


im.save("flag.png")
