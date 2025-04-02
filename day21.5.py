import datetime
dt=datetime.datetime(2019,12,13,14,44,45)
thirtyears=datetime.timedelta(days=365*30)
print(dt-thirtyears)
print(dt-(2*thirtyears))
print(dt+thirtyears)