#coding:utf-8
def getShopName(tmpResult,resultMap):
  print('input shopName {}'.format(tmpResult))
  if(  tmpResult.find('art')>-1 \
    or tmpResult.find('巨')>-1 \
    or tmpResult.find('馬')>-1 \
    or tmpResult.find('M rt')>-1 \
    or tmpResult.find('Yar')>-1 \
    or tmpResult.find('am')>-1 \
    ):
      resultMap['1_shopName'] = 'ファミリマート'
      resultMap['pos_shop']=1
  elif(resultMap['type_shop']==1):
    if (tmpResult.find('Y!') > -1):
      resultMap['1_shopName'] = 'ファミマ!!'
    resultMap['1_shopName'] = 'ファミマ!!'
    resultMap['pos_shop']=1
  elif(  tmpResult.find('ルツ')>-1 \
    # or tmpResult.find('Yar')>-1 \
    # or tmpResult.find('am')>-1 \
    ):
      resultMap['1_shopName'] = 'サークルK'
      resultMap['1_shopName_test'] = 'unknown_shop_name'
      resultMap['pos_shop']=1

  if(resultMap['pos_shop']==1):
    print('output shopName------------- {}'.format(resultMap['1_shopName']))