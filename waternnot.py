import time
from win10toast import ToastNotifier
import datetime

s=(input("Enter your gender M/F:"))
wt=float(input("Enter your weight:"))
#ag=int(input("Enter your age:"))

if s=='M' or s=='m':
    if wt<45 and wt>=36:
        print("Drink minimum 1.4 litres water daily")
    elif wt<54 and wt>=45:
        print("Drink minimum 1.7 litres water daily")
    elif wt<64 and wt>=54:
        print("Drink minimum 2.0 litres water daily")
    elif wt<73 and wt>=64:
        print("Drink minimum 2.4 litres water daily") 
    elif wt<82 and wt>=73:
        print("Drink minimum 2.7 litres water daily")
    elif wt<91 and wt>=82:
        print("Drink minimum 2.9 litres water daily")
    elif wt<100 and wt>=91:
        print("Drink minimum 3.3 litres water daily")
    elif wt<109 and wt>=100:
        print("Drink minimum 3.5 litres water daily")
    elif wt<118 and wt>=109:
        print("Drink minimum 3.8 litres water daily")
    elif wt<127 and wt>=118:
        print("Drink minimum 4.1 litres water daily")
    elif wt<36:
        print("Drink minimum 1.2 litre water daily")
    else:
        print("Drinl more than 4.5 litres water daily")
    
elif s=='F' or s=='f':
    if wt<45 and wt>=36:
        print("Drink minimum 1.4 litres water daily")
    elif wt<54 and wt>=45:
        print("Drink minimum 1.7 litres water daily")
    elif wt<64 and wt>=54:
        print("Drink minimum 2.0 litres water daily")
    elif wt<73 and wt>=64:
        print("Drink minimum 2.4 litres water daily") 
    elif wt<82 and wt>=73:
        print("Drink minimum 2.7 litres water daily")
    elif wt<91 and wt>=82:
        print("Drink minimum 2.9 litres water daily")
    elif wt<100 and wt>=91:
        print("Drink minimum 3.3 litres water daily")
    elif wt<36:
        print("Drink minimum 1.2 litre water daily")
    else:
        print("Drink more than 3.7 litres water daily")
    
else:
    print("Incorrect gender")



print("NOTE: Drink as much as water you can,as it is helpful with no side effects")
print("Set your time limit for remainder")
def getTimeInput():
    hour = int(input("How many hours of interval before reminding :"))
    minutes = int(input("How many mins of interval before reminding :"))
    seconds = int(input("How many secs of interval before reminding :"))
    time_interval = seconds+(minutes*60)+(hour*3600)
    return time_interval
  
  
def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"Drank Water at: {now} \n")
    return 0
  
  
def notify():
    notification = ToastNotifier()
    notification.show_toast("ALERT:Time to drink water")
    log()
    return 0
  
  
def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify()
  
  
if __name__ == '__main__':
    time_interval = getTimeInput()
    starttime(time_interval)