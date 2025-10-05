import datetime
import time

for i in range(5):
    melon = datetime.datetime.now()
    print(melon.strftime("%H:%M:%S"))
    time.sleep(1)