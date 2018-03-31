#coding:utf-8
from receiptUtils import numberUtils
import re

def getCategory(sim_pred,resultMap,i):
  print('input_{} category {}'.format(i,sim_pred))
  iCategory=int(resultMap['6_category'])
  if(sim_pred.find('半')>-1):
    tmpCategory=sim_pred.split('半')[-1].replace(',','')
    tmpCategory= numberUtils.numberReplacement(tmpCategory)
    iCategory+=1
    resultMap['6_category'] = iCategory
  elif(sim_pred.find('羊')>-1):
    tmpCategory=sim_pred.split('羊')[-1].replace(',','')
    tmpCategory = numberUtils.numberReplacement(tmpCategory)
    iCategory += 1
    resultMap['6_category']=iCategory
  if(int(resultMap['6_category'])>0):
    print('output category {}'.format(resultMap['6_category']))

def getCategorySuffix(tmpResult,resultMap,key,tmpDict):
  if(tmpDict['tax']>0 and key>tmpDict['tax']-4):
    return
  if(tmpDict['year']>=key):
    return
  print('input_{} category {}'.format(key,tmpResult))
  if(tmpResult.find('半')>-1):
    tmpResult=tmpResult[tmpResult.find('半'):]
  elif(tmpResult.find('羊')>-1):
    tmpResult=tmpResult[tmpResult.find('羊'):]
  elif(tmpResult.find('洋')>-1):
    tmpResult=tmpResult[tmpResult.find('洋'):]
  elif(tmpResult.find('浄')>-1):
    tmpResult=tmpResult[tmpResult.find('浄'):]
  else:
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