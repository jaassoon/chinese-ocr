#coding:utf-8
from receiptUtils import numberUtils,priceUtils
import re,jaconv

def getCategoryAfter(tmpResult,resultMap,i):
  tmpResult = jaconv.z2h(tmpResult, digit=True, ascii=True)
  # not minus ｰ
  if(tmpResult.find('責')>-1 \
     or tmpResult.find('No')>-1 \
     or tmpResult.find('点')>-1 \
     or tmpResult.find('×')>-1 \
     # or tmpResult.find('-')>-1 \
     or tmpResult.find('ｰ')>-1 \
     or tmpResult.find(':')>-1 \
     or tmpResult.find('NO')>-1):
      return
  if not priceUtils.checkMnyStr(tmpResult):
      return
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

  if tmpResult.find('-')>-1:
      iCatPrice*=-1
  if(iCatPrice !=0):
    resultMap['suffix_catPrice'].append(iCatPrice)
    print('output iCatPrice------------- {}'.format(iCatPrice))