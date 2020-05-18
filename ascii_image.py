from PIL import Image
import pprint
import sys

ASCII_CHARS = ['#', '?', ' ', '.', '=', '+', '.', '*', '3', '&', '@']
fp = sys.argv[1]
# run the program in this format --- python ascii_image.py <your image file> ---


# open image
def open_image(file_path):
    image = Image.open(file_path)
    return image


# resize the image
# you can adjust the value of new_width. it's the width of your ascii image
# you can increase it to have a better view and
# you can decrease it to have a concise view
def scale_image(image, new_width=100):
    original_height, original_width = image.size
    aspect_ratio = original_height//original_width
    new_height = aspect_ratio*new_width
    resized_image = image.resize((new_width, new_height))
    return resized_image


# convert to grayscale
def convert_to_greyscale(image):
    grey_image = image.convert('L')
    grey_image.save('new_file.png')
    return grey_image


# convert pixels to ascii characters
def map_pixels_to_ascii(image, range_width=25):
    """
    maps each pixel into ascii characters based on the range it falls
    range_width: divides the ultimate intensity range of the pixel value, 0 - 255, into 25 sub-ranges
    range_width is used mainly to prevent the pixels_to_char comprehension from throwing error
    and ensure that pixels with the same pixel values have the same ascii values
    """
    pixels_to_char = []
    pixels_in_image = list(image.getdata())
    pixels_to_char = [ASCII_CHARS[int(pixel_value / range_width)] for pixel_value in pixels_in_image]
    pixel_char = "".join(pixels_to_char)
    return pixel_char


# convert the whole image to ascii
def image_to_ascii(image):
    new_width = 100
    image = scale_image(image)
    image = convert_to_greyscale(image)
    pixels_to_ascii_chars = map_pixels_to_ascii(image)
    len_pixels_to_ascii_chars = len(pixels_to_ascii_chars)
    image_ascii = [pixels_to_ascii_chars[index: index + new_width] for index in range(0, len_pixels_to_ascii_chars, new_width)]
    return "\n".join(image_ascii)


print(image_to_ascii(open_image(fp)))


