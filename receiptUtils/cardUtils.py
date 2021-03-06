#coding:utf-8
from receiptUtils import numberUtils
import re

def parseCard(resultMap, result):
    pos_card_after = resultMap['pos_card_after']
    if pos_card_after>0:
        getCardNo(str(result[pos_card_after][1]), resultMap, pos_card_after)
        if pos_card_after+1<len(result):
            getCardNo(str(result[pos_card_after+1][1]), resultMap, pos_card_after+1)
        if pos_card_after+2<len(result):
            getCardNo(str(result[pos_card_after+2][1]), resultMap, pos_card_after+2)
    if pos_card_after>1:
        getCardNo(str(result[pos_card_after-1][1]), resultMap, pos_card_after-1)

def getCardNo(tmpResult,resultMap,i):
  print('input card {}'.format(tmpResult))
  tmpResult=tmpResult.replace('冷','*').replace('米','*').replace('x','*').replace('深','*').replace('氷','*')\
      .replace('凍','*').replace('法','*').replace('※','*').replace('Q','0')
  if (tmpResult.find('***') > -1 and (tmpResult.find('TP') == -1 or \
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
        tmpHead=str(9)*(4-len(tmpHead))+tmpHead
    strList=re.findall(r'\d+', tmpTail)
    tmpTail=''.join(strList)
    if tmpTail=='':
        tmpTail='0000'
    if len(tmpTail)<4:
        tmpTail=str(1)*(4-len(tmpTail))+tmpTail

    tmpResult=tmpHead+'********'+tmpTail
    resultMap['8_pointcard'] = tmpResult
    resultMap['pos_card_after']=i
    print('output card-------------  {}'.format(tmpResult))

def getCardPos(resultMap, result):
    pos_ling_after = resultMap['pos_ling_after']
    pos_time_after = resultMap['pos_time_after']
    pos_tax_after = resultMap['pos_tax_after']

    for i in result:
        if pos_ling_after > 0 and i < pos_ling_after:
            continue
        if pos_time_after > 0 and i < pos_time_after:
            continue
        if pos_tax_after > 0 and i < pos_tax_after:
            continue
        if result[i][1].find('対条') > -1 \
                or result[i][1].find('会員') > -1 \
                or result[i][1].find('会具') > -1 \
                or result[i][1].find('会貝') > -1 \
                or result[i][1].find('番号') > -1 \
                or result[i][1].find('貝套') > -1 \
                or result[i][1].find('套号') > -1 \
                or result[i][1].find('具番') > -1 \
                or result[i][1].find('番写') > -1 \
                or result[i][1].find('員番') > -1 \
                or result[i][1].find('対策') > -1 \
                or result[i][1].find('策会') > -1 \
                or result[i][1].find('対象') > -1:
            resultMap['pos_card_after'] = i

    if (resultMap['pos_card_after'] > 0):
        print('output pos_card_after------------- {}'.format(resultMap['pos_card_after']))