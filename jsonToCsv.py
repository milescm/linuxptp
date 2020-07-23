#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import json
import os
import datetime

print("abc.json --> abc\n")
jsonfileName = input('Input JSON file name: ')

# File Path must be modified.
data = pd.read_json('./f_json/%s.json' %jsonfileName, lines=True)


# drop the column 1
data.drop(['__CURSOR', '_BOOT_ID', '_TRANSPORT', '_SYSTEMD_INVOCATION_ID','_MACHINE_ID', '_HOSTNAME','_SYSTEMD_OWNER_UID','_SYSTEMD_USER_SLICE','_SYSTEMD_USER_UNIT'], axis= 'columns', inplace=True)


# drop the column 2
data.drop(['_EXE', '_CMDLINE', '_CAP_EFFECTIVE','_SELINUX_CONTEXT','_AUDIT_SESSION','_AUDIT_LOGINUID', '_SYSTEMD_CGROUP','_SYSTEMD_UNIT', '_SYSTEMD_SLICE','PRIORITY' ], axis='columns', inplace=True)


# drop the column 3
data.drop(['_UID','SYSLOG_FACILITY','SYSLOG_IDENTIFIER','_GID','_COMM','_PID','_SOURCE_REALTIME_TIMESTAMP'], axis='columns', inplace=True)

# split the message
delete_msg = []
for i in data['MESSAGE']:
    delete_msg.append(i.split())


# Make pandas data frame (['MESSAGE'])
dm = pd.DataFrame(delete_msg)


# find the system log message, index
cnt = 0
delete_rownum = []
for i in dm[1]:
    if(i!='master'):
        delete_rownum.append(cnt)
    cnt+=1

# delete row has system log message

dm = dm.drop(delete_rownum)
dm = dm.reset_index(drop=True)

data = data.drop(delete_rownum)
data = data.reset_index(drop=True)

# Convert Epoch time to human-readable date
hdate = []
for i in data['__REALTIME_TIMESTAMP']:
    s = str(i)
    hdate.append(int(s[0:10]))


# datetime could get only integer as parameter
dtime = pd.to_datetime(hdate, unit='s')
minAndsec = dtime.strftime('%M:%S')

# Add column UTC
data['UTC'] = minAndsec


# Make series to table value
offset = pd.DataFrame(dm)[3]
freq = pd.DataFrame(dm)[6]
delay = pd.DataFrame(dm)[9]

df = pd.concat([offset,freq,delay],axis=1, keys=['Master Offset', 'Frequency', 'Path Delay'])


# drop the column for concat original value
data.drop(['MESSAGE'], axis='columns', inplace=True)


# concat two pandas data frame
finalDf = pd.concat([data,df], axis=1)


#convert str to int
finalDf = finalDf.astype({'Master Offset': 'int'})
finalDf = finalDf.astype({'Frequency': 'int'})
finalDf = finalDf.astype({'Path Delay': 'int'})


# Delete column with NaN
finalDf = finalDf.dropna(axis=1)



finalDf.to_csv('./%s.csv' %jsonfileName)

print("Csv file was created :",os.getcwd()+"/%s" %jsonfileName)


