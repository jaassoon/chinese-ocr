#coding:utf-8
def getNo(sim_pred,resultMap,i):
    print('input staffNo {}'.format(sim_pred))
    if(sim_pred.find('No')==-1):
        return sim_pred
    if(sim_pred.find(',')>-1):
      tmpStrs=sim_pred.split(',')[-1]
    elif(sim_pred.find('.')>-1):
      tmpStrs=sim_pred.split('.')[-1]
    elif(sim_pred.find('。')>-1):
      tmpStrs=sim_pred.split('。')[-1]
    tmpStrs.replace('l','1')
    resultMap['a_staffNO']=tmpStrs
    tmpList=sim_pred.split('-')
    # amend in last step
    resultMap['9_receiptNO']=tmpList[0][-1]+'-'+tmpList[-1][:4]
    print('output staffNo {}'.format(resultMap['a_staffNO']))
    print('output receiptNO {}'.format(resultMap['9_receiptNO']))
    resultMap['pos_staff']=i
    return sim_pred