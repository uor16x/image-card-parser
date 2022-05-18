import cv2
import numpy
import time
import os
import sys
import getopt
import base64

BACKGROUPD_THRESHOLD = 30

def read_image_arg():
  if len(sys.argv) != 2:
    print('Please pass base64 image as only argument')
    sys.exit(2)
  return sys.argv[1]

def b64_to_cv2_img(b64img):
  nparr = numpy.fromstring(base64.b64decode(b64img.split(',')[1]), numpy.uint8)
  return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def process_image(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (5,5),0)
  image_width, img_height = numpy.shape(image)[:2]
  background_threshold_level = gray[int(image_width/100)][int(image_width/2)]
  threshold_level = background_threshold_level + BACKGROUPD_THRESHOLD
  _, threshold_image = cv2.threshold(blur, threshold_level, 255, cv2.THRESH_BINARY)
  return threshold_image


def main():
    image = b64_to_cv2_img(read_image_arg())
    processed_image = process_image(image)
    print(image)


if __name__ == "__main__":
    main()