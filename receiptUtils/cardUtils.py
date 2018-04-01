#coding:utf-8
from receiptUtils import numberUtils
import re
def getCardNo(tmpResult,resultMap,i):
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
    resultMap['pos_card_after']=i
    print('output card {}'.format(tmpResult))