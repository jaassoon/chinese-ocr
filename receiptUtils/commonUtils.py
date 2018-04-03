#coding:utf-8
from receiptUtils import numberUtils
import re

def pos_ling_predict(i,sim_pred,resultMap):
  if(i>3 and resultMap['pos_ling']==0 and sim_pred.find('領')>-1):
    resultMap['pos_ling']=i