
from PIL import Image
import numpy as np
#[ 0  2  3  4  5 11 15 16]
mask = np.array(Image.open('a.png'))
img = np.array(Image.open('a.jpg'))
chk = np.ones(img.shape,dtype=img.dtype)
print(img.shape)
print(np.unique(mask))
# all the work done in these two lines
mask = mask[:,:,np.newaxis]
res = np.where(mask==2, chk, img)
res=np.array(res,dtype=img.dtype)
print(img.shape)
print(mask.shape)
print(res.shape)
result = Image.fromarray(res)
result.show()
result.save('image_with_segmentation.jpg')
