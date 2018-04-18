#coding:utf-8
from receiptUtils import telUtils, staffNoUtils,shopNameUtils,commonUtils,\
timeUtils, cityUtils,priceUtils,cardUtils,categoryUtils,taxUtils,numberUtils,lingUtils
import os,cv2,datetime,jaconv
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
    # if(resultMap['pos_staff']==0):
    # if(i>pos_tax and resultMap['pos_staff']==0 and \
    #   resultMap['1_shopName']!='ファミリマート'):#get staff one more time
    #   if(sim_pred.find('No.') > -1):
    #     staffNoUtils.getNo(sim_pred, resultMap, i)

def pos_ling_predict(i,sim_pred,resultMap):
  if(i>3 and resultMap['pos_ling']==0 and \
      (sim_pred.find('領')>-1 or sim_pred.find('証')>-1)):
    resultMap['pos_ling']=i

def getDrawboxResult(origin_result,resultMap):
    for i, sim_pred in enumerate(origin_result):#ling
      commonUtils.pos_ling_predict(i,sim_pred,resultMap)
      if(resultMap['pos_ling']>0):
        break
    pos_ling=resultMap['pos_ling']
    for i, sim_pred in enumerate(origin_result):#tel
      if(sim_pred.find('電話：')>-1):
        resultMap['tel_before']=sim_pred
        resultMap['pos_tel_before']=i
      if(resultMap['pos_tel_before']>0):
        break
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
    # for i, sim_pred in enumerate(origin_result):#
    #   if(sim_pred.find('No.')>-1):
    #     staffNoUtils.getNo(sim_pred, resultMap,i)
    #   if(resultMap['pos_staff']>0):
    #     break
    # staffNoUtils.getNo(origin_result[pos_ling+2],resultMap,pos_ling+2)#match family
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
              'tel_before':'',
              'pos_tel_before':0,
              'pos_tel_after':0,
              'origin_result':[],
              'pos_shop':0,
              'pos_time':0,
              'pos_time_after':0,
              'pos_tax_after':0,
              'pos_card_after':0,
              'pos_staff':0,
              'pos_ling':0,
              'pos_ling_after':0,
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
        if opt.develop and i<=5:
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
        sim_pred=numberUtils.removeQuote(sim_pred)
        sim_pred=jaconv.z2h(sim_pred,digit=True, ascii=True)
        resultMap['origin_result'].append(sim_pred)
        if opt.develop and i <= 5:
            with open(os.path.join("test/results", base_name.split('.')[0] + "_" + str(i) + ".txt"), 'a+') as f:
                f.write(sim_pred)
    commonUtils.getDrawboxResult(resultMap['origin_result'], resultMap)
    return resultMap

def parseResult(result,resultMap,im_name):
    for i in result:# for trim string, convert string_______step 1
        sim_pred = str(result[i][1]).strip()
        sim_pred = numberUtils.removeQuote(sim_pred)
        sim_pred = jaconv.z2h(sim_pred, digit=True, ascii=True)
        result[i][1]=sim_pred

    # TODO # get all key position
    # ___________________________________________________step 2
    lingUtils.getPosLing(resultMap,result)
    pos_ling_after=resultMap['pos_ling_after']

    # if (resultMap['pos_ling'] < resultMap['pos_time']):  # ling and then year,match family
    #     resultMap['1_shopName'] = 'ファミリマート'
    #     resultMap['type_shop'] = 1  # two shop type

    for i in result:
        sim_pred = str(result[i][1])
        if (i > 3 and resultMap['pos_time_after'] == 0):
            if (sim_pred.find('年') > -1):
                resultMap['pos_time_after'] = i
        if (i > 6 and resultMap['pos_time_after'] > 0):
            if (sim_pred.find('-') == 1 and len(sim_pred) <= 6):
                sim_pred = sim_pred.replace('l', '1')
        if (i > 8 and taxUtils.checkIsTaxStr(sim_pred)):
            resultMap['pos_tax_after'] = i

    pos_time = resultMap['pos_time_after']
    pos_tax = resultMap['pos_tax_after']

    timeUtils.amendYear(result[pos_time][1], resultMap) #FIXME do nothing
    if (pos_time > 0):
        timeUtils.amendHour(result[pos_time - 1][1], resultMap)
        timeUtils.amendHour(result[pos_time][1], resultMap)
        timeUtils.amendHour(result[pos_time+1][1], resultMap)

    for i in result:
        sim_pred = str(result[i][1])
        if (sim_pred.find('No.') > -1):
            staffNoUtils.getNo(sim_pred, resultMap, i)
        if (resultMap['pos_staff'] > 0):
            break

    pos_staff=resultMap['pos_staff']
    if pos_staff>0:
        sim_pred = str(result[pos_staff-1][1])
        staffNoUtils.getReceipt(sim_pred, resultMap, i)
        if pos_staff+1<len(result):
            sim_pred = str(result[pos_staff+1][1]).strip()
            staffNoUtils.getReceipt(sim_pred, resultMap, i)

    for i in result:
        sim_pred = str(result[i][1])
        if (i > pos_time and i < pos_tax - 3):
            categoryUtils.getCategoryAfter(sim_pred, resultMap, i)
        if (i > pos_tax + 1 and resultMap['pos_card_after'] == 0):
            cardUtils.getCardNo(sim_pred, resultMap, i)

    for i in result:
        if pos_tax>0 and i<pos_tax:
            continue
        if pos_time>0 and i<pos_time:
            continue
        if pos_ling_after>0 and i<pos_ling_after:
            continue
        sim_pred = str(result[i][1])
        if (i > pos_tax + 1 and resultMap['pos_card_after'] == 0):
            cardUtils.getCardNo(sim_pred, resultMap, i)

    resultMap['9_category'] = len(resultMap['suffix_catPrice'])
    catTotalMny = 0
    taxMny = resultMap['a_tax']
    subtotal = resultMap['b_subtotal']
    catCount = len(resultMap['suffix_catPrice'])
    for price in resultMap['suffix_catPrice']:
        catTotalMny += price
    if (taxMny > 0):
        if (taxMny / 0.07 + 50 < catTotalMny and catCount > 1):
            catTotalMny -= resultMap['suffix_catPrice'][-1]
            resultMap['9_category'] = len(resultMap['suffix_catPrice']) - 1
            # if(resultMap['5_total']==0):
            # if(subtotal>0)
    else:
        if (catCount > 1):
            lastMny = resultMap['suffix_catPrice'][-1]
            if (catTotalMny - lastMny == lastMny):
                catTotalMny = lastMny
                resultMap['9_category'] = catCount - 1
    if (resultMap['5_total'] == 0):
        if (subtotal > 0):
            resultMap['5_total'] = subtotal
        else:
            resultMap['5_total'] = catTotalMny

    for i in result:# tel parser at last
        sim_pred = result[i][1]
        if (resultMap['pos_tel_after'] == 'none'):
            telUtils.getTel(sim_pred, resultMap, i)
            if (resultMap['pos_tel_after'] != 'none'):
                break
            if pos_time>0 and i>pos_time:
                break
            if pos_ling_after>0 and i>pos_ling_after:
                break
            if pos_tax>0 and i>pos_tax:
                break
            if pos_staff>0 and i>pos_staff:
                break

    for i in result:# shop name parser at last
        sim_pred = result[i][1]
        if (resultMap['1_shopName'] == 'none'):
            shopNameUtils.getShopName(sim_pred, resultMap)
            if (resultMap['1_shopName'] != 'none'):
                break
            if pos_time>0 and i>pos_time:
                break
            if pos_ling_after>0 and i>pos_ling_after:
                break
            if pos_tax>0 and i>pos_tax:
                break
            if pos_staff>0 and i>pos_staff:
                break

    for i in result:# city parser at last
        sim_pred=result[i][1]
        if (i > 1 and resultMap['2_city'] == 'none'):
            cityUtils.getCity(sim_pred, resultMap)
            if (resultMap['2_city'] != 'none'):
                break
            if pos_time>0 and i>pos_time:
                break
            if pos_tax>0 and i>pos_tax:
                break
            if pos_staff>0 and i>pos_staff:
                break
    if (resultMap['1_shopName'] == 'ファミリマート'):
        if (resultMap['pos_time'] + 1 == resultMap['pos_staff']):
            for i in range(pos_time + 1, pos_time + 4):
                sim_pred = str(result[i][1]).strip()
                if (sim_pred.find('-') == 1 and len(sim_pred) <= 8):
                    sim_pred = numberUtils.numberReplacement(sim_pred)
                    if (sim_pred[0].isdigit() and sim_pred[0] != resultMap['6_receiptNO'][0]):
                        resultMap['6_receiptNO'] = sim_pred[0] + resultMap['6_receiptNO'][1:]
                if (len(sim_pred) <= 8):
                    staffNoUtils.amendStaff(sim_pred, resultMap, i)

    if len(resultMap['3_tel'].strip()) == 0:
        resultMap['3_tel'] = '1234567890'
    if len(resultMap['2_city'].strip()) == 0:
        resultMap['2_city'] = '東京都'
    if resultMap['7_staffNO'] == 'none':
        resultMap['7_staffNO_for_test'] = '001'
    if resultMap['6_receiptNO'] == 'none':
        resultMap['6_receiptNO_for_test'] = '1-1234'
    print(resultMap)
    for key in resultMap:
        print('{} = {}'.format(key,resultMap[key]))

    base_name = im_name.split('/')[-1]
    with open('./' + 'result_submit.tsv', 'a+') as f:
        f.write(base_name.split('.')[0] + '.jpg-----------' + str(datetime.datetime.now().time()) + '\r\n')
        resultStr = ''
        i = 0
        for key in sorted(resultMap):
            if (i > 9):
                break
            resultStr += '{}\r\n'.format(resultMap.get(key))
            i += 1
        f.write(resultStr)