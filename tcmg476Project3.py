
import os.path
import re
from datetime import date, datetime
import calendar

print("Please wait while the logs are downloaded")

# This function puts the log file in a file named thalogs.txt
def savelogs():
    if not os.path.exists('./thalogs.txt'):
        import urllib.request
        urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','thalogs.txt')

savelogs()

# This section will go through the log file and seperate the logs per month, and also find the error codes


def file_count():    
    print('Parsing log, and writing files by month. This will take a while.')
    
    num_lines = 0
    file_dict = {}
    date_dict = {}
    status_3 = []
    status_4 = []

    o94 = open('october_94.txt' , 'a')
    n94 = open('november_94.txt' , 'a')
    d94 = open('december_94.txt' , 'a')
    j95 = open('january_95.txt' , 'a')
    f95 = open('febuary_95.txt' , 'a')
    m95 = open('march_95.txt' , 'a')
    a95 = open('april_95.txt' , 'a')
    ma95 = open('may_95.txt' , 'a')
    ju95 = open('june_95.txt' , 'a')
    jul95 = open('july_95.txt' , 'a')
    au95 = open('august_95.txt' , 'a')
    s95 = open('september_95.txt' , 'a')
    o95 = open('october_95.txt' , 'a')

    for line in open('thalogs.txt'):
        num_lines += 1
        pieces = re.split('.*\\[([^:]*):(.*) \\-[0-9]{4}\\] \\"([A-Z]+) (.*)( HTTP.*\\") ([2-5]0[0-9] .*)', line)

        try:
            file = pieces[4]
            status = pieces[6]
            date = pieces[1]
        except IndexError:
            continue

        if file in file_dict:
            file_dict[file] += 1
        else:
            file_dict[file] = 1
        if date in date_dict:
            date_dict[date] += 1
        else:
            date_dict[date] = 1 

        date = str(pieces[1])
        month = re.findall(r'[A-Z][a-z][a-z]?\\d*',date)
        year = re.findall(r'[0-9]?\\d*',date)

#This is where the code seperates the log by month and wrights it to files according to the month and year
   
        if month == ['Oct'] and year[6] == '1994':
            o94.write(line)


        if month == ['Nov'] and year[6] == '1994':
            n94.write(line)


                
        if month == ['Dec'] and year[6] == '1994':
            d94.write(line)



        if month == ['Jan'] and year[6] == '1995': 
            j95.write(line)



        if month == ['Feb'] and year[6] == '1995':
            f95.write(line)


        if month == ['Mar'] and year[6] == '1995':
            m95.write(line)



        if month == ['Apr'] and year[6] == '1995':
            a95.write(line)



        if month == ['May'] and year[6] == '1995':
            ma95.write(line)



        if month == ['Jun'] and year[6] == '1995':
            ju95.write(line)



        if month == ['Jul'] and year[6] == '1995':
            jul95.write(line)



        if month == ['Aug'] and year[6] == '1995':
            au95.write(line)



        if month == ['Sep'] and year[6] == '1995':
            s95.write(line)



        if month == ['Oct'] and year[6] == '1995':
            o95.write(line)


    
        error = str(pieces[6])
        code = list(re.findall(r'[0-9]',error))
        first = code[0]
      
        if first == '3':
            status_3.append(first)
        elif first == '4':
            status_4.append(first)

  
    status_300 = len(status_3)
    status_400 = len(status_4)     

    percent300 = (status_300/726736) * 100
    percent400 = (status_400/726736) * 100

    print("The total percent of 400 requests that were not successful:            "  ,percent400)
    print("The total percent of 300 requests that were redirected elsewhere:      " ,percent300)

          
    avg_week = num_lines/50.4286
    avg_mon = num_lines/11.5921
    
    print('This is the total amount of requests in the log file: ',num_lines)
    print('This is the average amount of requests for a week: ', avg_week)
    print('This is the average amount of requests for a month: ', avg_mon)

    maximum = max(file_dict, key=file_dict.get)
    minimum = min(file_dict, key=file_dict.get)

    print('The most requested file is ', maximum,' with ', file_dict[maximum],' requests.')

    min_file = []
    for k in file_dict.keys():
        if file_dict.get(k) == 1:
            min_file.append(k)
        else:
            continue

    print('The most least requested file is',minimum)

    mon_req=[]
    tues_req=[]
    wed_req=[]
    thur_req=[]
    fri_req=[]
    sat_req=[]
    sun_req=[]
    day='placeholder'

    for d in date_dict.keys():
        datetime_obj=datetime.strptime(d, '%d/%b/%Y')
        day=calendar.day_name[datetime_obj.weekday()]
        if day=='Monday':
            mon_req.append(date_dict.get(d))
        elif day=='Tuesday':
            tues_req.append(date_dict.get(d))
        elif day=='Wednesday':
            wed_req.append(date_dict.get(d))
        elif day=='Thursday':
            thur_req.append(date_dict.get(d))
        elif day=='Friday':
            fri_req.append(date_dict.get(d))
        elif day=='Saturday':
            sat_req.append(date_dict.get(d))
        else:
            sun_req.append(date_dict.get(d))    

    avg_mon= sum(mon_req)/len(mon_req)
    avg_tues= sum(tues_req)/len(tues_req)
    avg_wed= sum(wed_req)/len(wed_req)
    avg_thur= sum(thur_req)/len(thur_req)
    avg_fri= sum(fri_req)/len(fri_req)
    avg_sat= sum(sat_req)/len(sat_req)
    avg_sun= sum(sun_req)/len(sun_req)

    print('The average monday has    ', avg_mon,  ' requests')
    print('The average tuesday has   ', avg_tues, ' requests')
    print('The average wednesday has ', avg_wed,  ' requests')
    print('The average thursday has  ', avg_thur, ' requests')
    print('The average friday has    ', avg_fri,  ' requests')
    print('The average saturday has  ', avg_sat,  ' requests')
    print('The average sunday has    ', avg_sun,  ' requests')


file_count()
input()