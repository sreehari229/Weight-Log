#!/usr/bin/env python

import sys
import pandas
import datetime

now_date = datetime.datetime.now()
current_value = float(sys.argv[1])

data = {
    'Datetime' : [now_date],
    'Weight' : [current_value]
}
dataframe = pandas.DataFrame(data)

dataframe.to_csv('logfile.csv', mode='a' , index=False, header=False)

print("Datetime = " , now_date)
print("Value = " , current_value)
print("------------- Added the above data in logfile.csv ----------------------")
