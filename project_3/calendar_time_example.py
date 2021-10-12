# calendar time example

import datetime
import calendar

my_rawdatetimes = ["01-Feb-2021 00:22:09.111", "09-Apr-1999 00:04:11.538", "07-Mar-2001 00:14:19.671"]

datetimes = []
for line in my_rawdatetimes:
    foo = line.split(" ",2)
    dmy = foo[0].split("-",2)
    d = dmy[0]
    mo = dmy[1]
    y = dmy[2]
    hms = foo[1].split(":",2)
    h = hms[0]
    mi = hms[1]
    mysec = hms[2].split(".",1)
    s = mysec[0]
    ms = mysec[1]
    mydatetime = datetime.datetime(int(y),list(calendar.month_abbr).index(mo),int(d),int(h),int(mi),int(s),int(ms)*1000)
    datetimes.append(mydatetime)
    
print("unsorted:")
for dt in datetimes:
    print(str(dt))

datetimes.sort()

print("\nsorted:")
for dt in datetimes:
    print(str(dt))



