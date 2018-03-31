#coding:utf-8
def getMny(sim_pred):
  if(sim_pred.find('半')>-1):
    sim_pred=sim_pred[sim_pred.find('半'):]
  elif(sim_pred.find('羊')>-1):
    sim_pred=sim_pred[sim_pred.find('羊'):]
  elif(sim_pred.find('毕')>-1):
    sim_pred=sim_pred[sim_pred.find('毕'):]
  elif(sim_pred.find('浄')>-1):
    sim_pred=sim_pred[sim_pred.find('浄'):]
  elif(sim_pred.find('平')>-1):
    sim_pred=sim_pred[sim_pred.find('平'):]
  elif(sim_pred.find('洋')>-1):
    sim_pred=sim_pred[sim_pred.find('洋'):]
  else:
    sim_pred=''
  return sim_pred

def numberReplacement(tmpResult):
  tmpResult = tmpResult\
      .replace('の', '0') \
      .replace('G', '0') \
      .replace('C', '0') \
      .replace('l', '1') \
      .replace('L', '1') \
      .replace(']', '1') \
      .replace('J', '1') \
      .replace('Z', '1') \
      .replace('?', '2') \
      .replace('z', '2') \
      .replace('A', '4')\
      .replace('F', '5') \
      .replace('S', '5') \
      .replace('e', '6') \
      .replace('B', '8')\
      .replace('&', '8')\
      .replace('日', '9')\
      .replace('目', '9')\
      .replace('月', '9')\
      .replace('g', '9')\
      .replace(':', '')\
      .replace('。', '')\
      .replace(',', '')\
      .replace('，', '')\
      .replace('、', '')\
      .replace('\'', '')\
      .strip('\'')\
      .replace(' ','')
  return tmpResult