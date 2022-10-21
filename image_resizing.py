from PIL import Image

image = Image.open("Pictures/menu_page.png")
new_image = image.resize((400, 400))
new_image.save('Pictures/menu_page.png')
new_image.show()
