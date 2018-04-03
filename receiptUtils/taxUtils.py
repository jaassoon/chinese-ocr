#coding:utf-8
from receiptUtils import numberUtils
import re

def getTax(sim_pred,resultMap,i):
  print('input_{} tax {}'.format(i,sim_pred))
  resultMap['pos_tax']=i
  sim_pred=numberUtils.getMny(sim_pred)
  sim_pred=numberUtils.numberReplacement(sim_pred)
  lstTax=re.findall(r'\d+', sim_pred)
  sTax=''.join(lstTax)
  if(sTax==''):
    iTax=0
  else:
    iTax=int(sTax)
  resultMap['a_tax']=iTax
  if(resultMap['a_tax']>0):
    print('output tax------------- {}'.format(resultMap['a_tax']))

def checkIsTaxStr(sim_pred):
  return (sim_pred.find('消') > -1 and sim_pred.find('税') > -1) \
    or (sim_pred.find('内') > -1 and sim_pred.find('等') > -1) \
    or (sim_pred.find('内') > -1 and sim_pred.find('税') > -1) \
    or (sim_pred.find('消') > -1 and sim_pred.find('等') > -1) \
    or (sim_pred.find('内消') > -1) \
    or (sim_pred.find('税等') > -1)

def pos_tax_predict(i,sim_pred,resultMap):
  if (i>resultMap['pos_ling'] and resultMap['pos_tax']==0 and \
    checkIsTaxStr(sim_pred)):
      resultMap['pos_tax']=i