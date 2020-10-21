import os
from skimage.io import imread
from skimage.transform import resize
import numpy as np
flat_data = []  #image pixel in flatten style
images = []

path = '/content/drive/My Drive/miniprojectimages/images/images'

for dirpath,dirnames,filenames in os.walk(path):
    for filename in filenames:

        category = dirpath.split('/')[-1]

        target.append(category)
        img =imread(f'{path}/{category}/{filename}')
        img_resize = resize(img,(50,50,3)) #Scaling down
        flat_data.append(img_resize.flatten())
        images.append(img_resize)


flat_data = np.array(flat_data)
target = np.array(target)
images = np.array(images)

print(flat_data.shape)
print(target)
a=1
while a ==1:
  print("enter png or jpg pic link of tiger or peacock")
  path=input()
  img =imread(path)

  test_flat_data=[]
  imgs=[]
  img_resize = resize(img,(50,50,3))
  test_flat_data.append(img_resize.flatten())
  imgs.append(img_resize)

  output=model.predict(test_flat_data)
  print(output)
  print("try another pic press 1\n else enter 0")
  a=int(input())
