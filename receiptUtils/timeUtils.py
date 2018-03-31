#coding:utf-8
import datetime,re
from receiptUtils import numberUtils

def getTimeStr(sim_pred,resultMap,i):
    print('input year {}'.format(sim_pred))
    sim_pred=sim_pred.replace(';',':')
    if(sim_pred.find('年')==-1):
        return sim_pred
    if(int(resultMap['pos_time'])>0):#return if already set
        return
    sim_pred=sim_pred.replace('年日','年9').replace('  ',' ')
    sim_pred=sim_pred.replace('目','日').replace('曰','日').replace('l','1').replace(';',':')
    sim_pred=sim_pred.replace('局','月').replace('l','1').replace(';',':')\
    .replace('時',':').replace('跨',':').replace('府',':')
    sim_pred=sim_pred.replace('》',' ').replace(')',' ') # yyyy-mm-dd x)Time

    sYear=sim_pred[0:sim_pred.find('年')]
    iPosYear=sim_pred.find('年')
    sYear=numberUtils.numberReplacement(sYear)
    lstYear=re.findall(r'\d+', sYear)
    sYear=''.join(sYear)
    if(len(sYear)!=4):
        sYear='2017'
    iYear=int(sYear)

    if(sim_pred.find('月')==-1):
        iMonth=1
    elif(sim_pred.find('月')>iPosYear+3):#maybe week
        iMonth=1
    else:
        sMonth=sim_pred[sim_pred.find('年'):sim_pred.find('月')]
        sMonth=numberUtils.numberReplacement(sMonth)
        lstMonth=re.findall(r'\d+', sMonth)
        sMonth=''.join(lstMonth)
        if(sMonth==''):
            iMonth=1
        else:
            iMonth=int(sMonth)

    if(iMonth>12 or iMonth==0):
        iMonth=1
#----------------------------------------
    if(sim_pred.find('日')==-1):
        iDate=1
    elif(sim_pred.find('日')>iPosYear+6):#maybe week
        iDate=1
    else:
        sDate=sim_pred[sim_pred.find('年'):sim_pred.find('日')]
        sDate=numberUtils.numberReplacement(sDate)
        sDate=sDate[-3:]
        lstDate=re.findall(r'\d+', sDate)
        sDate=''.join(lstDate)
        if(sDate==''):
            iDate=1
        else:
            iDate=int(sDate)

    if(iDate>31 or iDate==0):
        iDate=1
#----------------------------------------hour
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
#----------------------------------------minute
    if(sim_pred.find(':')==-1):
        iMin=0
    else:
        sMin=sim_pred[sim_pred.find(':'):]
        sMin=numberUtils.numberReplacement(sMin)
        lstMin=re.findall(r'\d+', sMin)
        sMin=''.join(lstMin)
        if(sMin==''):
            iMin=0
        else:
            iMin=int(sMin)

    if(iMin>59):
        iMin=0

    # print('year={},month={},date={},time={}'.format(iYear,iMonth,iDate,iHour))
    try:
        new_date = datetime.datetime(iYear, iMonth, iDate, iHour,iMin)
        new_date = str(new_date)
        resultMap['4_year']=new_date
        print('output year {}'.format(resultMap['4_year']))
        resultMap['pos_time']=i
    except:
        print('Exception for {}'.format(sim_pred))