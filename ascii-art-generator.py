from PIL import Image

def image_to_ascii(image_path, output_width=100):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height / float(width)
    output_height = int(output_width * aspect_ratio)
    image = image.resize((output_width, output_height))
    image = image.convert('L') # Convert to grayscale

    ascii_art = ""
    for y in range(output_height):
        for x in range(output_width):
            pixel = image.getpixel((x, y))
            ascii_art += ascii_chars[pixel // 25]
        ascii_art += '\n'
    return ascii_art

ascii_chars = '@%#*+=-:. '

image_path = 'example.jpg' # Replace with your image file path
output_width = 80

ascii_art = image_to_ascii(image_path, output_width)

with open('output.txt', 'w') as file:
    file.write(ascii_art)
