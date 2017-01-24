
from PIL import Image
import numpy as np
#[ 0  2  3  4  5 11 15 16]
mask = np.array(Image.open('segmentation.png'))
img = np.array(Image.open('dataset10k_1400.jpg'))
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
result.save('final.jpg')

'''
x =res *255
#plt.imshow(x, cmap='gray', interpolation='nearest', vmin=0, vmax=255)

  # Creates PIL image
img = Image.fromarray(x, 'L')
  #img.show()
  #print(np.unique(array_image))
  #Rescale to 0-255 and convert to uint8
data=x
rescaled = (255.0*data).astype(np.uint8)
  
im = Image.fromarray(rescaled)
save_image='final.png'
im.save(save_image)
  #im = Image.open('test.png')
  #in_ = np.array(im).astype('uint8')
  #print(np.unique(in_))
'''
