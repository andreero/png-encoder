"""
Decode input png image into a file
"""

import argparse
import os

from PIL import Image

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('input_file')
parser.add_argument('-o', metavar='output_file')
args = parser.parse_args()

outfile = args.o if args.o else os.path.splitext(args.input_file)[0]

with Image.open(args.input_file, 'r') as image, open(outfile, "wb") as outfile:
    width, height = image.size
    pixel_values = list(image.getdata())
    for x in range(width):
        for y in range(height):
            outfile.write(bytes(pixel_values[width * x + y]))
