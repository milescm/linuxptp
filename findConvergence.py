#!/usr/bin/env python
# coding: utf-8


import pandas as pd


# read text file

print("abc.txt --> abc\n")
txtfileName = input("Input txt file name : ")


# File Path must be modified.
f = open('./f_txt/%s.txt' %txtfileName, 'r')


# read line, split Str
tmp_str = []

while True:
    line = f.readline()
    if not line: break
    tmp_str.append(line.split())   


# Make series for concat value
offset = pd.DataFrame(tmp_str)[3]
freq = pd.DataFrame(tmp_str)[6]
delay = pd.DataFrame(tmp_str)[9]


# make table
df = pd.concat([offset,freq,delay],axis=1, keys=['Master Offset', 'Frequency', 'Path Delay'])


# Delete row has null value
df.isnull().sum()
df.dropna(inplace=True)
df = df.reset_index(drop=True)


#convert str to int
df = df.astype({'Master Offset': 'int'})
df = df.astype({'Frequency': 'int'})
df = df.astype({'Path Delay': 'int'})


# Add abs master offset column to df
absMasterOffset = []

absMasterOffset = df['Master Offset'].abs()

df['Abs Master Offset'] = absMasterOffset


# Find the convergence index, master offset

cnt = 0
index = 0
for i in df['Abs Master Offset']:
    if(cnt > 11):
        print("%s.txt =" %txtfileName,"Convergence index :", index , " Master Offset :", df['Master Offset'][index])
        break
    else:
        if(i <= 1000):
            cnt += 1
        else:
            if(cnt < 0):
                cnt = 0
            else:
                cnt -= 1
    index+=1


