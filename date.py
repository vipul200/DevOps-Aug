import datetime as dt

# date object of today's date
today = dt.date.today() 

data_year=("{}".format(today.year))
data_mon = str(((int("{}".format(today.month)))-1))
print(data_mon)
search = '{0}/0{1}'.format(data_year,data_mon)
print(search)

#search ='2023/07'
#print(search)
bkp_date = dt.datetime.today().strftime('%Y%m%d')
#print("bkp_date : ", bkp_date)
