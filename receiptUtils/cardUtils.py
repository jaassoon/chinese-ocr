#coding:utf-8
from receiptUtils import numberUtils

def getCardNo(tmpResult,resultMap,key,tmpDict):
    print('input card {}'.format(tmpResult))
    if (tmpResult.find('******') > -1 and tmpResult.find('TP') == -1):
        tmpResult=numberUtils.numberReplacement(tmpResult)
        resultMap['8_pointcard'] = tmpResult
        tmpDict['pos_card']=key
        print('output card {}'.format(tmpResult))
    return resultMap