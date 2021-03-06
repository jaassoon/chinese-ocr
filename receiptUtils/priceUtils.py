#coding:utf-8
from receiptUtils import numberUtils
import re

def getTotalPrice(sim_pred,resultMap,i):
  print('input_{} totalPrice {}'.format(i,sim_pred))
  resultMap['pos_total']=i
  sim_pred=numberUtils.getMny(sim_pred)
  sim_pred=numberUtils.numberReplacement(sim_pred)
  lstTotal=re.findall(r'\d+', sim_pred)
  sTotal=''.join(lstTotal)
  if(sTotal==''):
      iTotal=0
  else:
      iTotal=int(sTotal)
  resultMap['5_total']=iTotal
  if(resultMap['5_total']>0):
    print('output total------------- {}'.format(resultMap['5_total']))

def getSubTotalPrice(sim_pred,resultMap,i):
  print('input_{} subTotalPrice {}'.format(i,sim_pred))
  resultMap['pos_subtotal']=i
  sim_pred=numberUtils.getMny(sim_pred)
  sim_pred=numberUtils.numberReplacement(sim_pred)
  lstTotal=re.findall(r'\d+', sim_pred)
  sTotal=''.join(lstTotal)
  if(sTotal==''):
      iTotal=0
  else:
      iTotal=int(sTotal)
  resultMap['b_subtotal']=iTotal
  if(resultMap['b_subtotal']>0):
    print('output total------------- {}'.format(resultMap['b_subtotal']))

def checkMnyStr(sim_pred):
    return sim_pred.find('半') > -1 \
        or (sim_pred.find('￥') > -1) \
        or (sim_pred.find('羊') > -1) \
        or (sim_pred.find('毕') > -1) \
        or (sim_pred.find('浄') > -1) \
        or (sim_pred.find('平') > -1) \
        or (sim_pred.find('洋') > -1)
