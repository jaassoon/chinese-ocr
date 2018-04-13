#coding:utf-8
import model
from glob import glob
import numpy as np
from PIL import Image
import time,argparse
im_names = glob('./test/*.jpg')

parser = argparse.ArgumentParser()
parser.add_argument('--develop', action='store_true', help='to gen result img')
parser.add_argument('--torch', action='store_true', help='to use torch model')

opt = parser.parse_args()

def printOriginResult(result):
    with open('./' + 'result_origin.txt', 'a+') as f:
        strResult = ''
        for key in result:
            strResult += '{}\r\n'.format(result[key][1])
        f.write(strResult)

if __name__ =='__main__':
    for im_name in im_names:
      im = Image.open(im_name)
      img = np.array(im.convert('RGB'))
      t = time.time()
      print(im_name + "---------------------------------------")
      result,img,angle = model.model(img,opt,model='keras',im_name=im_name)
      print("It takes time:{}s".format(time.time() - t))
      if opt.develop:
        printOriginResult(result)