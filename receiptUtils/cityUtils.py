#coding:utf-8
def getCity(tmpResult,resultMap):
    print('input city {}'.format(tmpResult))
    if(tmpResult.find('兵')==0):
        resultMap['2_city']='兵庫県'
    elif(tmpResult.find('京都府')>-1):
        resultMap['2_city']='京都府'
    elif(tmpResult.find('宫城')>-1):
        resultMap['2_city']='宮城県'
    elif(tmpResult.find('爱知')>-1):
        resultMap['2_city']='愛知県'
    elif(tmpResult.find('良')>-1):
        resultMap['2_city']='奈良県'
    elif(tmpResult.find('神')>-1 and tmpResult.find('川')>0):
        resultMap['2_city']='神奈川県'
    elif(tmpResult.find('京都')>0):
        resultMap['2_city']='東京都'
    elif(tmpResult.find('大')==0 and tmpResult.find('府')>0):
        resultMap['2_city'] = '大阪府'
    print('output city {}'.format(resultMap['2_city']))
    return resultMap
