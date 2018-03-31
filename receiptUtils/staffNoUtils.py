#coding:utf-8
from receiptUtils import numberUtils
import re

def getNo(sim_pred,resultMap,i):
    if(sim_pred.find('No')==-1 and sim_pred.find('責')==-1 and sim_pred.find('黄')==-1):
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
    resultMap['a_staffNO']=tmpStrs

    tmpList=sim_pred.split('-')
    tmpHead=tmpList[0]
    lstHead=re.findall(r'\d+', tmpHead)
    tmpHead=''.join(lstHead)
    if(tmpHead==''):
        tmpHead='1'
    tmpTail=tmpList[-1][:4]
    lstTail=re.findall(r'\d+', tmpTail)
    tmpTail=''.join(lstTail)

    resultMap['9_receiptNO']=tmpHead+'-'+tmpTail
    print('output staffNo {}'.format(resultMap['a_staffNO']))
    print('output receiptNO {}'.format(resultMap['9_receiptNO']))
    resultMap['pos_staff']=i
