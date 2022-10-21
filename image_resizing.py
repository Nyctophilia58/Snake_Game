from PIL import Image

image = Image.open("Pictures/collide.png")
new_image = image.resize((700, 700))
new_image.save('Pictures/collide.png')
new_image.show()
