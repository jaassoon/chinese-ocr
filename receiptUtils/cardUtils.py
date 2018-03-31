#coding:utf-8
from receiptUtils import numberUtils
import re
def getCardNo(tmpResult,resultMap,key,tmpDict):
  if(tmpDict['tax']>0 and (key<tmpDict['tax']+5 or key>tmpDict['tax']+7)):
    return
  print('input card {}'.format(tmpResult))
  tmpResult=tmpResult.replace('冷','*').replace('米','*').replace('x','*')
  if (tmpResult.find('******') > -1 and tmpResult.find('TP') == -1):
    tmpResult=numberUtils.numberReplacement(tmpResult)
    if(tmpResult.find('号')>-1):
        tmpResult=tmpResult.split('号')[1]
    tmpHead=tmpResult[0:tmpResult.find('*')]
    tmpTail=tmpResult[tmpResult.rfind('*'):]
    strList=re.findall(r'\d+', tmpHead)
    tmpHead=''.join(strList)

    strList=re.findall(r'\d+', tmpTail)
    tmpTail=''.join(strList)
    tmpResult=tmpHead+'********'+tmpTail
    resultMap['8_pointcard'] = tmpResult
    tmpDict['pos_card']=key
    print('output card {}'.format(tmpResult))