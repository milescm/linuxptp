#!/bin/bash --login

echo "This process will stop after 5min"

# Start ptp4l sync

## The log values(offset, freq, path delay) are overwritten in the text file.
sudo ptp4l -i eth0 -m >> /home/rtst15/AutoCheckTimeStamping/f_txt/ptpTime5min_4.txt &


## Waits 5 minutes.
sleep 5m


## Kill "ptp4l" process in linux
sudo kill -9 `ps -ef | grep ptp4l | grep -v grep | awk '{print $2}'`



## If "JSON" file exits, save it so that files do not overlap
for ((i=1;i<=10;i++))
do
	if [[ -e "/home/rtst15/AutoCheckTimeStamping/f_json/ptpTime5min_$i.json" ]]; then
		continue
	else
		sudo journalctl --since "-5min" --until "-2s" -o json > /home/rtst15/AutoCheckTimeStamping/f_json/ptpTime5min_"$((i))".json
		echo "Json file was created succesfully"
	       break
       fi
done






	

