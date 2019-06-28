"""
Encode input file into a square png image
"""

import argparse

from PIL import Image
from math import ceil, sqrt

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('input_file')
parser.add_argument('-o', metavar='output_file')
args = parser.parse_args()

outfile = args.o if args.o else args.input_file + '.png'

with open(args.input_file, 'rb') as infile:
    byte_array = infile.read()
    length = len(byte_array)
    side = int(ceil(sqrt(length / 3)))
    bytes_needed = int(side * side * 3)
    if length < bytes_needed:
        byte_array += bytearray(bytes_needed - length)
    image = Image.frombytes('RGB', (side, side), byte_array)
    image.save(outfile, 'png')
