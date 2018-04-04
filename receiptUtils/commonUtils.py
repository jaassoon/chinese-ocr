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