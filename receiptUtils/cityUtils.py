#coding:utf-8
def getCity(tmpResult,resultMap):
    print('input city {}'.format(tmpResult))
    tmpResult=tmpResult.strip().replace(',','').replace('，','').replace('\'','')
    if(tmpResult.find('兵')==0):
        resultMap['2_city']='兵庫県'
    elif(tmpResult.find('京都府')>-1):
        resultMap['2_city']='京都府'
    elif(tmpResult.find('宮城')>-1 or (tmpResult.find('城')>-1 and tmpResult.find('城')<3)):
        resultMap['2_city']='宮城県'
    elif(tmpResult.find('香川')>-1 or tmpResult.find('杳')>-1):
        resultMap['2_city']='香川県'
    elif(tmpResult.find('愛知')>-1 or tmpResult.find('知県')>-1):
        resultMap['2_city']='愛知県'
    elif(tmpResult.find('三重')>-1):
        resultMap['2_city']='三重県'
    elif(tmpResult.find('歧阜')>-1):#FIXME
        resultMap['2_city']='岐阜県'
    elif(tmpResult.find('山口')>-1):
        resultMap['2_city']='山口県'
    elif(tmpResult.find('玉')>-1):
        resultMap['2_city']='埼玉県'
    elif(tmpResult.find('良')>-1):
        resultMap['2_city']='奈良県'
    elif(tmpResult.find('静')>-1):
        resultMap['2_city']='静岡県'
    elif(tmpResult.find('福固')>-1):
        resultMap['2_city']='福岡県'
    elif(tmpResult.find('秋田')>-1):
        resultMap['2_city']='秋田県'
    elif(tmpResult.find('滋')>-1):
        resultMap['2_city']='滋賀県'
    elif(tmpResult.find('神')==0 or (tmpResult.find('神')>-1 and tmpResult.find('川')>0)):
        resultMap['2_city']='神奈川県'
    elif(tmpResult.find('哀京都')>-1 or (tmpResult.find('京都')>-1 and tmpResult.find('府')!=2)):
        resultMap['2_city']='東京都'
    elif(tmpResult.find('鹿')>0):
        resultMap['2_city']='鹿児島県'
    elif(tmpResult.find('和歌山')>0):
        resultMap['2_city']='和歌山県'
    elif(tmpResult.find('ナ阪')>-1 or (tmpResult.find('大')==0 and tmpResult.find('府')>0)):
        resultMap['2_city'] = '大阪府'
    else:
        resultMap['2_city'] = tmpResult[:3]
    print('output city {}'.format(resultMap['2_city']))
    return resultMap
