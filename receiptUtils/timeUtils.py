#coding:utf-8
def getTimeStr(sim_pred,resultMap,i):
    print('input year {}'.format(sim_pred))
    if(sim_pred.find('年')==-1):
        return sim_pred
    if(sim_pred.find(':')==-1):
        return sim_pred
    sim_pred=sim_pred.replace('目','日').replace('l','1').replace(';',':')
    sim_pred=sim_pred.replace('局','月').replace('l','1').replace(';',':')
    timeList = sim_pred.split(' ')
    sYear = timeList[0]
    sMonth = sYear.split('年')[1]
    sMonth = sMonth.split('月')[0]
    sDate = sYear.split('月')[1]
    sDate = sDate.split('日')[0]
    if(len(timeList)==2):# yyyy-mm-dd x)Time
        sTime = timeList[1].split(')')[1]
    else:
        sTime = timeList[2]
    import datetime
    sYear.replace('?','2')
    sMonth.replace('?','2')
    sDate.replace('?','2')
    sTime.replace('?','2')
    new_date = datetime.datetime(int(sYear[:4]), int(sMonth), int(sDate), int(sTime.split(':')[0]),
                                 int(sTime.split(':')[1]))
    new_date = str(new_date)
    resultMap['4_year']=new_date
    print('output year {}'.format(resultMap['4_year']))
    resultMap['pos_time']=i
    return new_date