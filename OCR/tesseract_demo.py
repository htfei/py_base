#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
#from PIL import ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES = True  # 解决问题OSError: image file is truncated

image = Image.open('test.png')
print(image)
code = pytesseract.image_to_string(image)
print(code)

