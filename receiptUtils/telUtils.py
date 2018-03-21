#coding:utf-8
def getTel(tmpResult,resultMap):
    print('input tel {}'.format(tmpResult))
    tmpResult=tmpResult.split(' ')[-1]
    tmpResult=tmpResult.replace('-','')
    if(tmpResult.find(':') > 0):
        tmpResult=tmpResult.split(':')[-1]
    tmpResult = tmpResult.replace('l','1').replace('A','4')
    tmpResult = tmpResult.replace('月','9').replace(']','1')
    tmpResult = tmpResult.replace(':','').replace('g','9')
    tmpResult = tmpResult.replace('e','6')
    resultMap['3_tel'] = tmpResult
    print('output tel {}'.format(tmpResult))
    return resultMap