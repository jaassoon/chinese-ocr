#coding:utf-8
from receiptUtils import numberUtils
import re,jaconv

def getTel(tmpResult,resultMap,i):
  print('input tel {}'.format(tmpResult))
  if(tmpResult.find('年')>-1):
      return
  if(resultMap['pos_tel_before']>0 and tmpResult.find(' ')>-1):
    print('tel_before {}'.format(resultMap['pos_tel_before']))
    telBefore=resultMap['tel_before'].split(':')
    if(len(telBefore)>1):
      telBeforeNew=telBefore[1]
      telAfter=tmpResult.split(':')
      if(len(telAfter)>1):
        telAfterNew=telAfter[1]
        lsStr1 = list(telAfterNew)
        for idx, val in enumerate(telAfterNew):
          if (val == ' '):
            lsStr1[idx] = telBeforeNew[idx]

  tmpResult = jaconv.z2h(tmpResult, digit=True, ascii=True)

  if(tmpResult.find('話')>-1):
      tmpResult=tmpResult.split('話')[1]
  if(tmpResult.find(':')>-1):
      tmpResult=tmpResult.split(':')[1]
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