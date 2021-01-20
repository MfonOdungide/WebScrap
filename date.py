from datetime import datetime,timedelta,date

GMT = -5

def timepy(current_time):
    current_time = datetime.strptime(current_time, '%H:%M:%S')
    print(current_time.time())
    time1 = (current_time + timedelta(hours=GMT))
    new_time = time1.time()
    return new_time


current_time = "20:30:00"


new_time = timepy(current_time)
print(new_time)
# new_time = timepy(current_time)

today_date_time = datetime.today()
tomorrow_date_time = datetime.today()+timedelta(days=1)
today_time = datetime.now()

now_time = today_time.strftime("%H:%M")

today_date = today_date_time.strftime("%Y-%m-%d")
tomorrow_date = tomorrow_date_time.strftime("%Y-%m-%d")

url_today = "http://www.statarea.com/predictions/date/"+today_date+"/competition"
print (url_today)

url_tomorrow = "http://www.statarea.com/predictions/date/"+tomorrow_date+"/competition"
print (url_tomorrow)

print(now_time)

if now_time < "20:00":
    print("Not yet time")
elif now_time > "20:00":
    print("Time is past")
else:
    print("Unknown time")




def time_check_filename():
    today_date_time = datetime.today()
    tomorrow_date_time = datetime.today()+timedelta(days=1)
    today_time = datetime.now()

    now_time = today_time.strftime("%H:%M")
    today_date = today_date_time.strftime("%Y-%m-%d")
    tomorrow_date = tomorrow_date_time.strftime("%Y-%m-%d")

    if now_time < "20:00":
        date = today_date_time.strftime("%d%b%Y")
        # return str(today_date) 
        # print("Not yet time")
    elif now_time > "20:00":
        date = tomorrow_date_time.strftime("%d%b%Y")
        # return str(tomorrow_date) 
        # print("Time is past")
    else:
        date = "FootyGuru"
        # return unknown
    return date


day = time_check_filename()
print("new string is",day)