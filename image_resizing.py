from PIL import Image

image = Image.open("Pictures/game_screen.png")
new_image = image.resize((700, 700))
new_image.save('Pictures/game_screen.png')
new_image.show()
