#coding:utf-8
def convertFromStr(tmpResult):
  tmpResult=tmpResult.replace('l','1')
  return tmpResult

def numberReplacement(tmpResult):
  tmpResult = tmpResult\
      .replace('G', '0') \
      .replace('l', '1') \
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