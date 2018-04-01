#coding:utf-8
resultMap={'1_shopName':'ファミア!!','2_city':'none',
              '3_tel':'1234567890','4_year':'none',
              '5_goods':'none','6_category':0,
              '7_total':0,'8_pointcard':'none',
              '9_receiptNO':'none','a_staffNO':'none',
              'a_tax':0,
              'suffix_catPrice':[],
              'pos_tel_after':0,
              'origin_result':[],
              'pos_shop':0,
              'pos_time':0,
              'pos_time_after':0,
              'pos_tax_after':0,
              'pos_card_after':0,
              'pos_staff':0,
              'pos_ling':0,
              'pos_category':0,
              'pos_total':0,
              'pos_tax':0,
              'pos_card':0}
def checkIsTaxStr(sim_pred):
  return (sim_pred.find('消') > -1 and sim_pred.find('税') > -1) \
      or (sim_pred.find('内') > -1 and sim_pred.find('等') > -1) \
      or (sim_pred.find('内') > -1 and sim_pred.find('税') > -1) \
      or (sim_pred.find('消') > -1 and sim_pred.find('等') > -1) \
      or (sim_pred.find('内消') > -1) \
      or (sim_pred.find('税等') > -1)
      
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