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
