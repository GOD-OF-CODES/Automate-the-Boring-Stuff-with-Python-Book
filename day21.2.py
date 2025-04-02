import time
print("press enter to begin. afterwards, press enter to 'click' the stopwatch. press c to quit")
input()
print("started")
starttime=time.time()
lastime=starttime
lapnum=1
try:
    while True:
        input()
        laptime=round(time.time()-lastime,2)
        totaltime=round(time.time()-starttime,2)
        print('Lap #%s: %s (%s)' % (lapnum,totaltime,laptime),end='')
        lapnum+=1
        lastime=time.time()
except KeyboardInterrupt:
    print()
    print('Done')