import cv2
import numpy
import time
import os
import sys
import getopt
import base64

def read_image_arg():
  if len(sys.argv) != 2:
    print('Please pass base64 image as only argument')
    sys.exit(2)
  return sys.argv[1]

def b64_to_cv2_img(b64img):
  nparr = numpy.fromstring(base64.b64decode(b64img.split(',')[1]), numpy.uint8)
  return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def main():
    image = b64_to_cv2_img(read_image_arg())
    print(image)


if __name__ == "__main__":
    main()