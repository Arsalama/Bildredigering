from PIL import Image, ImageOps

image = Image.open("geo.png")
image = image.convert("L")                        
img = ImageOps.mirror(image)
img = ImageOps.posterize(img, 2)
img.save("geo_posterize.png")


