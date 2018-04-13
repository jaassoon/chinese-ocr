#coding:utf-8
from receiptUtils import telUtils, staffNoUtils,shopNameUtils,commonUtils,\
timeUtils, cityUtils,priceUtils,cardUtils,categoryUtils,taxUtils,numberUtils
import os,cv2
import numpy as np
from PIL import Image

def adjustPredict(i,sim_pred,resultMap,pos_tax):
    # ---------------------------------subtotal
    if(i>=pos_tax-3 and i<pos_tax-1 and resultMap['pos_subtotal']==0 \
      and sim_pred.find('小') > -1):
      priceUtils.getSubTotalPrice(sim_pred,resultMap,i)
    # ---------------------------------total
    if(i>pos_tax-2 and i<pos_tax and sim_pred.find('合') > -1):
      priceUtils.getTotalPrice(sim_pred,resultMap,i)
    # ---------------------------------staff
    if(i>pos_tax and resultMap['pos_staff']==0 and \
      resultMap['1_shopName']!='ファミリマート'):#get staff one more time
      if(sim_pred.find('No.') > -1):
        staffNoUtils.getNo(sim_pred, resultMap, i)

def pos_ling_predict(i,sim_pred,resultMap):
  if(i>3 and resultMap['pos_ling']==0 and sim_pred.find('領')>-1):
    resultMap['pos_ling']=i

def getDrawboxResult(origin_result,resultMap):
    for i, sim_pred in enumerate(origin_result):#ling
      commonUtils.pos_ling_predict(i,sim_pred,resultMap)
      if(resultMap['pos_ling']>0):
        break
    pos_ling=resultMap['pos_ling']
    for i, sim_pred in enumerate(origin_result):#tax
      taxUtils.pos_tax_predict(i,sim_pred,resultMap)
      if(resultMap['pos_tax']>0):
        break
    for i, sim_pred in enumerate(origin_result):#year
      if(resultMap['pos_time']>0 and i<=3 and i>=pos_ling+2):
        break
      if(sim_pred.find('年') > -1):
        timeUtils.getTimeStr(sim_pred, resultMap, i)

    pos_tax=resultMap['pos_tax']
    taxUtils.getTax(origin_result[pos_tax],resultMap,pos_tax)
    staffNoUtils.getNo(origin_result[pos_ling+2],resultMap,pos_ling+2)#match family
    for i, sim_pred in enumerate(origin_result):
        commonUtils.adjustPredict(i,sim_pred,resultMap,pos_tax)

def draw_boxes(img,image_name,boxes,opt,adjust):
    base_name = image_name.split('/')[-1]
    i=0
    j=0
    boxes = sorted(boxes, key=lambda x: x[1])
    boxesX0 = sorted(boxes, key=lambda x: x[0])
    xStart=boxesX0[0][0]
    iXStart=int(xStart)
    if(iXStart<0):
        iXStart=0
    boxesX2 = sorted(boxes, key=lambda x: x[2])
    xEnd=boxesX2[-1][2]
    previousY=0
    resultMap={'1_shopName':'ファミア!!','2_city':'none',
              '3_tel':'1234567890','4_year':'none',
              '5_total':0,
              '6_receiptNO':'none',
              '7_staffNO':'none',
              '8_pointcard':'none',
              '9_category':0,
              'a_goods':'none',

              'a_tax':0,
              'b_subtotal':0,
              'suffix_catPrice':[],
              'pos_tel_after':0,
              'origin_result':[],
              'pos_shop':0,
              'pos_time':0,
              'pos_time_after':0,
              'pos_tax_after':0,
              'pos_card_after':0,
              'pos_staff':0,
              'pos_ling':0,
              'pos_category':0,
              'pos_total':0,
              'pos_subtotal':0,
              'pos_tax':0,
              'pos_card':0,
              'type_shop':0}
    for box in boxes:
        if np.linalg.norm(box[0] - box[1]) < 5 or np.linalg.norm(box[3] - box[0]) < 5:
            j+=1
            continue
        if(i>0 and int(box[1])-previousY<=11):
            previousY=int(box[1])
            continue
        previousY = int(box[1])
        i+=1
        crop_img = img[int(box[1]):int(box[5]), iXStart:int(xEnd)]
        # print('Y0={}, Y1={}, X0={}, X1={}'.format(int(box[1]),int(box[5]),iXStart,int(xEnd)))
        if opt.develop:
          cv2.imwrite(os.path.join("test/results", base_name.split('.')[0] + "_" + str(i) + ".jpg"), crop_img)
        try:
            if opt.torch:
              from crnn.crnn import crnnOcr
              sim_pred = crnnOcr(Image.fromarray(crop_img ).convert('L')).strip()
            else:
              from ocr.model import predict as ocr
              sim_pred = ocr(Image.fromarray(crop_img ).convert('L')).strip()
        except Exception as e:
            print('Exception for step {}--{}'.format(i,e))
            continue
        sim_pred=sim_pred.strip()
        resultMap['origin_result'].append(sim_pred)
    commonUtils.getDrawboxResult(resultMap['origin_result'], resultMap)
    return resultMap
