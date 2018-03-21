#coding:utf-8
from receiptUtils import numberUtils

def getTel(tmpResult,resultMap):
    print('input tel {}'.format(tmpResult))
    tmpResult=tmpResult.split(' ')[-1]
    tmpResult=tmpResult.replace('-','')
    if(tmpResult.find(':') > 0):
        tmpResult=tmpResult.split(':')[-1]
    tmpResult=tmpResult.replace(' ','')
    if(len(tmpResult)>10):
        tmpResult=tmpResult[-10:-1]
    tmpResult = numberUtils.numberReplacement(tmpResult)
    resultMap['3_tel'] = tmpResult
    print('output tel {}'.format(tmpResult))
    return resultMap