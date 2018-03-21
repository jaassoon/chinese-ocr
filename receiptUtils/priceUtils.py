#coding:utf-8
def getTotalPrice(sim_pred,resultMap,i):
  print('input totalPrice {}'.format(sim_pred))
  if(sim_pred.find('小')==0):
    totalFlg=False
    if(sim_pred.find('半')>-1):
      tmpTotal=sim_pred.split('半')[-1].replace('l','1')
      resultMap['7_total']=tmpTotal
      resultMap['pos_total']=i+1
      totalFlg=True
    elif(sim_pred.find('羊')>-1):
      tmpTotal=sim_pred.split('羊')[-1].replace('l','1')
      resultMap['7_total']=tmpTotal
      resultMap['pos_total']=i+1
      totalFlg=True
    if(totalFlg and resultMap['pos_staff']>0):
      resultMap['6_category']=i-resultMap['pos_staff']
  print('output totalPrice {}'.format(resultMap['7_total']))
  return resultMap