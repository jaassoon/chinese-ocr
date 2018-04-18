#coding:utf-8
import datetime,re
from receiptUtils import numberUtils

def getYear(sim_pred):
  sYear=sim_pred[0:sim_pred.find('年')]
  sYear=numberUtils.numberReplacement(sYear)
  lstYear=re.findall(r'\d+', sYear)
  sYear=''.join(lstYear)
  if(len(sYear)!=4):
    sYear='2017'
  if int(sYear)>2019 or int(sYear)<2016:
      sYear='2017'
  return int(sYear)

def getMonth(sim_pred):
  iPosYear=sim_pred.find('年')
  iPosMonth=sim_pred.find('月')
  if(iPosMonth==-1):
      iMonth=1
  elif(iPosMonth>iPosYear+3):#maybe week
      iMonth=1
  else:
      sMonth=sim_pred[iPosYear+1:iPosMonth]
      sMonth=numberUtils.numberReplacement(sMonth)
      lstMonth=re.findall(r'\d+', sMonth)
      sMonth=''.join(lstMonth)
      if(sMonth==''):
          iMonth=1
      else:
          iMonth=int(sMonth)
  if(iMonth>12 or iMonth==0):
    iMonth=1
  return iMonth

def getDay(sim_pred):
  iPosYear=sim_pred.find('年')
  iPosDay=sim_pred.find('日')
  if(iPosDay==-1):
    iDay=1
  elif(iPosDay>iPosYear+6):#maybe week
    iDay=1
  else:
    sDay=sim_pred[iPosDay-2:iPosDay]
    sDay=numberUtils.numberReplacement(sDay)
    lstDate=re.findall(r'\d+', sDay)
    sDay=''.join(lstDate)
    if(sDay==''):
      iDay=1
    else:
      iDay=int(sDay)

  if(iDay>31 or iDay==0):
    iDay=1
  return iDay

def getHour(sim_pred):
  if(sim_pred.find(':')==-1):
    iHour=0
  else:
    sHour=sim_pred[sim_pred.find(':')-2:sim_pred.find(':')]
    sHour=numberUtils.numberReplacement(sHour)
    sHour=sHour[-3:]
    lstHour=re.findall(r'\d+', sHour)
    sHour=''.join(lstHour)
    if(sHour==''):
        iHour=0
    else:
      iHour=int(sHour)
  if(iHour>23):
    iHour=0
  return iHour

def getMin(sim_pred):
  if(sim_pred.find(':')==-1):
    iMin=0
  else:
    sMin=sim_pred[sim_pred.find(':')+1:]
    sMin=numberUtils.numberReplacement(sMin)
    lstMin=re.findall(r'\d+', sMin)
    sMin=''.join(lstMin)
    if(sMin==''):
      iMin=0
    else:
      iMin=int(sMin)
  if(iMin>59):
    iMin=0
  return iMin

def amendYear(sim_pred,resultMap):#2017-11-01 00:49:00
  sTime=resultMap['4_year']
  sim_pred=replaceTime(sim_pred)
  iYear=getYear(sim_pred)
  iMonth=getMonth(sim_pred)
  iDay=getDay(sim_pred)
  iHour=getHour(sim_pred)
  iMin=getMin(sim_pred)

def amendHour(sim_pred,resultMap):#2017-11-01 00:49:00
  sTime=resultMap['4_year']
  if sTime=='none':
      sTime='2017-01-01 00:00:00'
  print('output year before amend time {}'.format(sim_pred))
  if(sim_pred.find('領')>-1 \
     or sim_pred.find('収')>-1 \
     or sim_pred.find('ｰ')>-1 \
     or sim_pred.find('責')>-1 \
     or sim_pred.find('No')>-1 \
     or sim_pred.find('NO')>-1 \
     or sim_pred.find('書')>-1 \
     or sim_pred.find('証')>-1):
    print('output year before amend time,return due to...')
    return
  sim_pred=replaceTime(sim_pred)
  iYear = getYear(sim_pred)

  sim_pred=sim_pred[sim_pred.find('年')+1:]
  sim_pred=sim_pred.replace('/',':')
  iMonth=getMonth(sim_pred)
  iDay=getDay(sim_pred)
  iHour=getHour(sim_pred)
  iMin=getMin(sim_pred)

  sTime = str(iYear)+sTime[4:]
  if(iMonth>0 and sTime[5:7]=='01'):
    sMonth=str(iMonth)
    if(iMonth<10):
        sMonth='0'+sMonth
    sTime=sTime[0:5]+sMonth+sTime[7:]

  if(iDay>0 and sTime[8:10]=='01'):
    sDay=str(iDay)
    if(iDay<10):
        sDay='0'+sDay
    sTime=sTime[0:8]+sDay+sTime[10:]

  if(iHour>0 and sTime[11:13]=='00'):
    sHour=str(iHour)
    if(iHour<10):
      sHour='0'+sHour
    sTime=sTime[0:11]+sHour+sTime[13:]

  if(iMin>0 and sTime[14:16]=='00'):
    sMin=str(iMin)
    if(iMin<10):
      sMin='0'+sMin
    sTime=sTime[0:14]+sMin+sTime[16:]
  resultMap['4_year']=sTime
  print('output year after amend time {}'.format(resultMap['4_year']))

def replaceTime(sim_pred):
  sim_pred=sim_pred.replace('年日','年9').replace('  ',' ')\
    .replace('目','日').replace('曰','日').replace('巴','日').replace('回','日').replace('l','1').replace(';',':')\
    .replace('局','月').replace('l','1').replace('ﾕ','1').replace(';',':')\
    .replace('時',':').replace('跨',':').replace('府',':')\
    .replace('》',' ').replace(')',' ') # yyyy-mm-dd x)Time
  return sim_pred

def getTimeStr(sim_pred,resultMap,i):
    print('input year {}'.format(sim_pred))
    sim_pred=sim_pred.replace(';',':')
    if(sim_pred.find('年')==-1):
        return sim_pred
    if(int(resultMap['pos_time'])>0):#return if already set
        return
    sim_pred=replaceTime(sim_pred)

    new_date = datetime.datetime(getYear(sim_pred),getMonth(sim_pred)\
      ,getDay(sim_pred),getHour(sim_pred),getMin(sim_pred))
    resultMap['4_year']=str(new_date)
    print('output year {}'.format(resultMap['4_year']))
    resultMap['pos_time']=i
