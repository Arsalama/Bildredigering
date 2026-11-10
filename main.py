from PIL import Image, ImageEnhance

image = Image.open("geo.png")

image = image.convert("L")

image.save("new file")




