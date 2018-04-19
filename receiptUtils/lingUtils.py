#coding:utf-8
from receiptUtils import numberUtils
import re

def getPosLing(resultMap,result):
  for i in result:
      if resultMap['pos_ling_after'] > 0:
          break
      if result[i][1].find('領 証') > -1 \
          or result[i][1].find('領収') > -1 \
          or result[i][1].find('収証') > -1 \
          or result[i][1].find('領 書') > -1 \
          or result[i][1].find('収書') > -1:
          resultMap['pos_ling_after'] = i

  if(resultMap['pos_ling_after']>0):
    print('output pos_ling_after------------- {}'.format(resultMap['pos_ling_after']))