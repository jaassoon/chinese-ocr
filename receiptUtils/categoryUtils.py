#coding:utf-8
from receiptUtils import numberUtils

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
  return resultMap