#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time,sys
im_names = glob('./test/*.jpg')

def printOriginResult(result):
    with open('test/' + 'result_origin.txt', 'a+') as f:
        strResult = ''
        for key in result:
            strResult += '{}\r\n'.format(result[key][1])
        f.write(strResult)
if __name__ =='__main__':
    lineNo=0
    devFlg=False
    if (len(sys.argv) > 1):
        devFlg=True
    for im_name in im_names:
      im = Image.open(im_name)
      img = np.array(im.convert('RGB'))
      t = time.time()
      print(im_name + "---------------------------------------")
      # result,img,angle,lineNo = model.model(img,lineNo,model='torch',im_name=im_name)
      result,img,angle,lineNo = model.model(img,lineNo,devFlg,model='keras',im_name=im_name)
      print("It takes time:{}s".format(time.time() - t))
      if(devFlg):
          printOriginResult(result)