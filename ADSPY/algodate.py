import datetime

def jour():
    
    d = datetime.date.today()
    z = d.strftime('%d-%b-%Y')
    
    #print(d)
    
    #Pour les pubs vues dans les 3 et 7 deriers jours !
    timedeltaday_3 = datetime.timedelta(days=3)
    timedeltaday_7 = datetime.timedelta(days=7)

    # Pour les pubs créees il a 3 ou 4 semaines !
    timedeltaweek_3 = datetime.timedelta(weeks=3)
    timedeltaweek_4 = datetime.timedelta(weeks=4)
    
    # 3 jours
    x_3 = d - timedeltaday_3
    x_3 = x_3.strftime('%d-%b-%Y')
    
    # 7 jours
    x_7 = d - timedeltaday_7
    x_7 = x_7.strftime('%d-%b-%Y')
    #print('7ème dernier jour :', x_7_jour)
    #print(x_7_jour.strftime('%d-%b-%Y'))
    
   # 3 semaines 
    y_3 = d - timedeltaweek_3
    y_3 = y_3.strftime('%d-%b-%Y')
   
   # 4 semaines
    y_4 = d - timedeltaweek_4
    y_4 = y_4.strftime('%d-%b-%Y')
    #print("jour d'il y a 3 dernères semaines :", y_3_semaines)
    #print(y_3_semaines.strftime('%d-%b-%Y'))
    
    
    ''' 
        print('year :', d.year)
        print('month :',d.month)
        print('day :',d.day)
        print('isoweekday :',d.isoweekday())
        print('weekday :',d.weekday())
    '''

    
    return x_3, x_7, y_3, y_4, z
    
    #d1 = d.strftime('%d-%b-%Y')
    #print(d1)
    #15-Dec-2020
date = jour()
x_3, x_7, y_3, y_4, z = date
#print(x)
#print(y)