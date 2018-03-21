#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time
im_names = glob('./test/*.jpg')

if __name__ =='__main__':
    for im_name in im_names:
      im = Image.open(im_name)
      img = np.array(im.convert('RGB'))
      t = time.time()
      result,img,angle = model.model(img,model='keras',im_name=im_name)
      print("It takes time:{}s".format(time.time()-t))
      print(im_name+"---------------------------------------")
      for key in result:
          print(result[key][1])
