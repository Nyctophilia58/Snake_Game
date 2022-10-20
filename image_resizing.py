from PIL import Image

image = Image.open("Pictures/Git.png")
new_image = image.resize((60, 60))
new_image.save('Pictures/Git.png')
new_image.show()
