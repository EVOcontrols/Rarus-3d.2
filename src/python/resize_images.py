from PIL import Image
import os
import shutil
import glob
from typing import Literal

Theme = Literal['dark', 'light']

targetWidth = 700
imagesPath = '../../public/slides'
targetFolder = f'{imagesPath}/medium'
themes: list[Theme] = ['dark', 'light']

def resize_image(filePath: str, theme: Theme):
  image = Image.open(filePath)
  w, h = image.size
  targetHeight = round((targetWidth / w) * h)
  resized = image.resize((targetWidth, targetHeight))
  filename = os.path.basename(filePath)
  resized.save(f'{targetFolder}/{theme}/{filename}')

def go():
  if os.path.exists(targetFolder):
    shutil.rmtree(targetFolder)

  os.mkdir(targetFolder)
  os.mkdir(f'{targetFolder}/dark')
  os.mkdir(f'{targetFolder}/light')
  # resize_image(5, 're')
  for theme in themes:
    files = glob.glob(f'{imagesPath}/full-size/{theme}/*')
    for file in files:
      resize_image(file, theme)
      # break
    # break

go()
# print(os.path.basename(files[0]))