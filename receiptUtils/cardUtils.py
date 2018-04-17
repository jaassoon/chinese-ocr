#coding:utf-8
from receiptUtils import numberUtils
import re
def getCardNo(tmpResult,resultMap,i):
  print('input card {}'.format(tmpResult))
  tmpResult=tmpResult.replace('冷','*').replace('米','*').replace('x','*')
  if (tmpResult.find('******') > -1 and (tmpResult.find('TP') == -1 or \
    tmpResult.find('ト') == -1)):
    tmpResult=numberUtils.numberReplacement(tmpResult)
    if(tmpResult.find('号')>-1):
        tmpResult=tmpResult.split('号')[1]
    tmpHead=tmpResult[0:tmpResult.find('*')]
    tmpTail=tmpResult[tmpResult.rfind('*'):]
    strList=re.findall(r'\d+', tmpHead)
    tmpHead=''.join(strList)
    if tmpHead=='':
        tmpHead='1234'
    if len(tmpHead)<4:
        tmpHead=str(1)*(4-len(tmpHead))+tmpHead
    strList=re.findall(r'\d+', tmpTail)
    tmpTail=''.join(strList)
    if tmpTail=='':
        tmpTail='1234'
    if len(tmpTail)<4:
        tmpTail=str(1)*(4-len(tmpTail))+tmpTail

    tmpResult=tmpHead+'********'+tmpTail
    # if(tmpHead=='' or tmpTail==''):
    #   return
    resultMap['8_pointcard'] = tmpResult
    resultMap['pos_card_after']=i
    print('output card {}'.format(tmpResult))