from PIL import Image
import os.path
import pathlib
import glob
import plac # para pedir un path
from pathlib import Path


from os import listdir
from os.path import isfile, join

@plac.annotations(
    dir=("Optional directory", "option", "o", Path),
)
def main(dir=Path('.')):
    print('This script will check if width and height of images in the same path are multiples of 2 \n')
    """Review images in this path."""
    # image_files = [f for f in dir.glob(['*.png','*.jpeg','*.jpg'])]
    image_files = []
    image_files.extend(dir.glob('*.png'))
    image_files.extend(dir.glob('*.jpeg'))
    image_files.extend(dir.glob('*.jpg'))
    # print(image_files)

    files_to_review = []

    for f in image_files:
        img = Image.open(f)
        width, height = img.size
        # print(f.name,'Dimensions:', img.size, 'Total pixels:', width * height)

        if not(width % 2 == 0 and height % 2 == 0):
            files_to_review.append(f)
            print(u"\u001b[31m X", u"\u001b[37m",f.name,'Dimensions:', img.size, 'Total pixels:', width * height)
            # print ('Added to list')
        else:
            print(u"\u001b[32m O", u"\u001b[37m",f.name,'Dimensions:', img.size, 'Total pixels:', width * height)

    if len(files_to_review) > 0:
        print ('\n The following image(s) need to be reviewed')
        for f in files_to_review:
            print(u"\u001b[31m X ", f, 'Review size image! \n', u"\u001b[37m")
    else:
        print("Everything seems ok! \n")
      
    

if __name__ == "__main__":
    plac.call(main)
    print("Press any key to exit")
    input()
