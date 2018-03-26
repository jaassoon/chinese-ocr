#coding:utf-8
from receiptUtils import numberUtils

def getTotalPrice(sim_pred,resultMap,i):
  print('input_{} totalPrice {}'.format(i,sim_pred))
  if(sim_pred.find('小')==0):
    totalFlg=False
    if(sim_pred.find('半')>-1):
      tmpTotal=sim_pred.split('半')[-1]
      tmpTotal= numberUtils.numberReplacement(tmpTotal)
      resultMap['7_total']=tmpTotal
      resultMap['pos_total']=i+1
      totalFlg=True
    elif(sim_pred.find('羊')>-1):
      tmpTotal=sim_pred.split('羊')[-1]
      tmpTotal = numberUtils.numberReplacement(tmpTotal)
      resultMap['7_total']=tmpTotal
      resultMap['pos_total']=i+1
      totalFlg=True
    # if(totalFlg and resultMap['pos_staff']>0):
    #   resultMap['6_category']=i-resultMap['pos_staff']
  try:
    if(int(resultMap['7_total'])>0):
      print('output totalPrice {}'.format(resultMap['7_total']))
  except:
    print('exception for resultMap[7_total]={}'.format(resultMap['7_total']))
  return resultMap