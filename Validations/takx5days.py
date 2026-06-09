from datetime import datetime
import datetime as dt
import pytz
from pytz import timezone

def gmtx(dateto):
    format='%Y-%m-%dT%H:%M:%S'
    a_d=datetime.strptime(dateto,format)
    #print(a_d)
    local = pytz.timezone("Etc/Greenwich")

    b_d = local.localize(a_d,is_dst=None)
    #print(b_d)
    utc_ts=b_d.astimezone(pytz.utc).timestamp()
    #print(utc_ts)
    utc_int=int(utc_ts)
    datef= utc_int*1000
    return datef

gmtx("2022-12-3T12:00:00")
print("2022-12-3T12:00:00")
#print(gmtx("2022-12-3T12:00:00"))



datesap=float(gmtx("2022-12-03T12:00:00")/1000)
nd=datetime.fromtimestamp(datesap).strftime("%Y %m %d %H:%M:%S")
print(nd)



date_1 = dt.datetime.strptime(nd, "%Y %m %d %H:%M:%S")

end_date = date_1  + dt.timedelta(days=10)
print(end_date)
strdate = str(end_date)

datefinal = strdate.split(" ")
datefinal1= datefinal[0]+"T"+datefinal[1]
print(datefinal1)