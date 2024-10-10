# pip install rembg

from rembg import remove
from PIL import Image

input_path = "/raz.jpg"
output_path = "output.png"

input = Image.open(input_path)
output = remove(input)

output.save(output_path)