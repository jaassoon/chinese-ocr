#coding:utf-8
from receiptUtils import numberUtils
import re

def getTel(tmpResult,resultMap,i):
  print('input tel {}'.format(tmpResult))
  tmpResult = numberUtils.numberReplacement(tmpResult)
  strList=re.findall(r'\d+', tmpResult)
  tmpResult=''.join(strList)
  if(len(tmpResult)>10):
    tmpResult=tmpResult[-10:-1]
  if(resultMap['3_tel']=='1234567890'):#init value
    resultMap['3_tel'] = tmpResult
  elif(len(resultMap['3_tel'])<len(tmpResult)):
    resultMap['3_tel'] = tmpResult
  if(resultMap['3_tel']==tmpResult and len(tmpResult)>6):
    print('output tel{} {}'.format('-'*10,tmpResult))
    if(tmpResult!='1234567890'):
      resultMap['pos_tel_after']=i