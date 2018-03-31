#coding:utf-8
import datetime
from receiptUtils import numberUtils

def getTimeStr(sim_pred,resultMap,i):
    print('input year {}'.format(sim_pred))
    sim_pred=sim_pred.replace(';',':')
    if(sim_pred.find('年')==-1):
        return sim_pred
    if(sim_pred.find(':')==-1):
        return sim_pred
    if(int(resultMap['pos_time'])>0):
        return
    sim_pred=sim_pred.replace('年日','年9').replace('  ',' ')
    sim_pred=sim_pred.replace('目','日').replace('曰','日').replace('l','1').replace(';',':')
    sim_pred=sim_pred.replace('局','月').replace('l','1').replace(';',':')
    sim_pred=sim_pred.replace('》',' ').replace(')',' ') # yyyy-mm-dd x)Time
    timeList = sim_pred.split(' ')
    if(len(timeList)>3):
        return
    sYear = timeList[0] # YYYY-MM-DD
    sMonth = sYear.split('年')[1] # MM-DD
    sMonth = sMonth.split('月')[0]

    sDate = sYear.split('月')[1] # DD-XX
    sDate = sDate.split('日')[0]

    sTime=''
    if(len(timeList)==2):
        sTime = timeList[1]
    elif(len(timeList)==3):
        sTime = timeList[2]

    if(sTime.find('分')>-1):
        sTime=sTime.replace('分','').replace('跨',':').replace('府',':')
    sYear=numberUtils.numberReplacement(sYear)
    sMonth=numberUtils.numberReplacement(sMonth)
    sDate=numberUtils.numberReplacement(sDate)

    iMonth=int(sMonth)
    if(iMonth>12 or iMonth<1):
        iMonth=1

    tmpTime=sTime.split(':')
    sHour=numberUtils.numberReplacement(tmpTime[0])
    if(sHour==''):
        sHour=1
    if(len(tmpTime)>1):
        sMin=numberUtils.numberReplacement(tmpTime[1])
        if(sMin==''):
            sMin=0
    else:
        sMin=0
    print('year={},month={},date={},time={}'.format(sYear,sMonth,sDate,sTime))
    try:
        new_date = datetime.datetime(int(sYear[:4]), iMonth, int(sDate), int(sHour),int(sMin))
        new_date = str(new_date)
        resultMap['4_year']=new_date
        print('output year {}'.format(resultMap['4_year']))
        resultMap['pos_time']=i
    except:
        print('Exception for {}'.format(sim_pred))
    # return new_date