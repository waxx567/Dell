# Importing required modules
from PIL import Image
from PIL import ImageOps
# Opening the image as an object
orig_img = Image.open("road.jpg")
# Flipping it vertically and saving the result
vert_img = ImageOps.flip(orig_img)
vert_img.save("vertflip.jpg")
# Flipping it horizontally and saving the result
horz_img = ImageOps.mirror(orig_img)
horz_img.save("horzflip.jpg")
# Closing all image objects
orig_img.close()
vert_img.close()
horz_img.close()