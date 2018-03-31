#coding:utf-8
def getShopName(tmpResult,resultMap):
  print('input shopName {}'.format(tmpResult))
  resultMap['1_shopName']='ファミア!!'
  if(  tmpResult.find('art')>-1 \
    or tmpResult.find('Yar')>-1 \
    or tmpResult.find('am')>-1 \
    ):
      resultMap['1_shopName'] = 'ファミリマート'
  print('output shopName {}'.format(resultMap['1_shopName']))
  return resultMap