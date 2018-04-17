#coding:utf-8
from receiptUtils import numberUtils
import re

def getCategoryAfter(tmpResult,resultMap,i):
  print('input_{} category {}'.format(i,tmpResult))
  tmpResult=numberUtils.getMny(tmpResult)
  if(tmpResult==''):
    return

  tmpResult=numberUtils.numberReplacement(tmpResult)
  lstCatPrice=re.findall(r'\d+', tmpResult)
  sCatPrice=''.join(lstCatPrice)
  if(sCatPrice==''):
    iCatPrice=0
  else:
    iCatPrice=int(sCatPrice)
  if(iCatPrice>0):
    resultMap['suffix_catPrice'].append(iCatPrice)
    print('output iCatPrice------------- {}'.format(iCatPrice))