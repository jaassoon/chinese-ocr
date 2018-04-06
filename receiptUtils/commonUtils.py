#coding:utf-8
from receiptUtils import telUtils, staffNoUtils,shopNameUtils,commonUtils,\
timeUtils, cityUtils,priceUtils,cardUtils,categoryUtils,taxUtils,numberUtils
import re

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