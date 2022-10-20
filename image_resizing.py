from PIL import Image

image = Image.open("Pictures/background.png")
new_image = image.resize((900, 900))
new_image.save('Pictures/background.png')
new_image.show()
