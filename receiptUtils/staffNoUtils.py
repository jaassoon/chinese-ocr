#coding:utf-8
from receiptUtils import numberUtils
import re

def isStaffStr(sim_pred):
    return sim_pred.find('No')>-1 or sim_pred.find('責')>-1 or sim_pred.find('黄')>-1

def amendStaff(sim_pred,resultMap,i):
  if(not isStaffStr(sim_pred)):
    return
  print('input staffNo_amend {}'.format(sim_pred))
  staffNoOrigin=resultMap['7_staffNO']
  sim_pred=sim_pred.replace(',','.').replace('。','.').replace('黄','責')
  if(sim_pred.find('.')>-1):
    tmpStrs=sim_pred.split('.')[-1]
  elif(sim_pred.find('責')>-1):
    tmpStrs=sim_pred.split('責')[-1]
  else:
    return
  tmpStrs=numberUtils.numberReplacement(tmpStrs)
  lstStaff=re.findall(r'\d+', tmpStrs)
  tmpStrs=''.join(lstStaff)
  if(len(tmpStrs)>=2):
    resultMap['7_staffNO']=tmpStrs
    print('output staffNo_amend {}'.format(resultMap['7_staffNO']))

def getNo(sim_pred,resultMap,i):
    if(not isStaffStr(sim_pred)):
      return
    print('input staffNo {}'.format(sim_pred))
    sim_pred=sim_pred.replace(',','.').replace('。','.').replace('黄','責')
    if(sim_pred.find('.')>-1):
      tmpStrs=sim_pred.split('.')[-1]
    elif(sim_pred.find('責')>-1):
      tmpStrs=sim_pred.split('責')[-1]
    else:
      return
    tmpStrs=numberUtils.numberReplacement(tmpStrs)
    lstStaff=re.findall(r'\d+', tmpStrs)
    tmpStrs=''.join(lstStaff)
    resultMap['7_staffNO']=tmpStrs

    tmpList=sim_pred.split('-')
    tmpHead=tmpList[0]
    lstHead=re.findall(r'\d+', tmpHead)
    tmpHead=''.join(lstHead)
    if(tmpHead==''):
        tmpHead='1'
    tmpTail=tmpList[-1][:4]
    lstTail=re.findall(r'\d+', tmpTail)
    tmpTail=''.join(lstTail)

    resultMap['6_receiptNO']=tmpHead+'-'+tmpTail
    print('output staffNo {}'.format(resultMap['7_staffNO']))
    print('output receiptNO {}'.format(resultMap['6_receiptNO']))
    resultMap['pos_staff']=i
