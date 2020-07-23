# Introduction
This files used the Precision Time Protocol(PTP) according to IEEE standard 1588 for Linux.

It contains log files that are generated at a specified time and analyzed and visualized.

# Envorinment
Master OS : Ubuntu20.04LTS

Slave OS : Ubuntu18.04LTS

python version : 3.6

Slave Bash version : 4.4.20



# Precondition
The **PATH** in the code must be modified according to the user's system.

The **master computer's ptp4l service** must always be running.


# How to Use
1. Run **run.sh** in the terminal commmand.
```sh
./run.sh
```

![runsh](https://user-images.githubusercontent.com/33818414/88164312-ecc3ed00-cc4e-11ea-8611-8e0c6b922fde.png)
- When the shell code ends, check the **created txt and JSON files**.


2. Run **findConvergence.py** in the terminal command.
```sh
./findConvergence.py
```

![findconvergence](https://user-images.githubusercontent.com/33818414/88164325-f188a100-cc4e-11ea-86bd-05f1b6e6fc15.png)
- ***You need to view the contents of the code and modify the PATH of the txt file***

- This python code analyzes a txt file and outputs the **index and offset of the converged section.**


3. Run **jsonToCsv.py** in the terminal command.
- This python code converts log files output in JSON format to **csv files**.
```sh
./jsonTocsv.py
```

![jsontocsv](https://user-images.githubusercontent.com/33818414/88164338-f51c2800-cc4e-11ea-8b02-a79a21311d3b.png)

- ***You need to view the contents of the code and modify the PATH of the JSON file***


4. Run **csv_Visualization.ipynb** in the jupyter-notebook
- This file **visualizes the data** via csv file.
 ```sh
 jupyter-notebook
 ```
 - ***You need to view the contents of the code and modify the PATH of the csv file***




# File Configuration

## run.sh
This shell code runs on the slave. 

This program runs the 'ptp4l' service for 5min and stops it.

The log of the service is saved as a txt file and a JSON file through redirection.

(Use journalctl to print the system log as a JSON file.)

The JSON file has TIMESTAMP, but the txt file has no time variable.


## findConvergence.py
When the offset is constant below 1000, set to convergence.

This file compares the offset values of the txt file and judges that it is convergence.

## jsonToCsv.py
This file converts JSON file to csv.


## csv_Visualization.ipynb
This file visualizes the data.


### Result
![allTime](https://user-images.githubusercontent.com/33818414/88252332-be92eb80-cce8-11ea-9105-0a3b4ac8b50f.png)


#### 0-30 sec
![0-30](https://user-images.githubusercontent.com/33818414/88252338-c2267280-cce8-11ea-9afd-9d2ed175be4c.png)


#### 31-60 sec
![31-60](https://user-images.githubusercontent.com/33818414/88252341-c3f03600-cce8-11ea-8bc7-89c0af266fe7.png)


#### 61--90 sec
![60-90](https://user-images.githubusercontent.com/33818414/88252342-c6529000-cce8-11ea-83b6-aa1776d850e9.png)

The purple line is the convergence section


#### 90 - 
![90-](https://user-images.githubusercontent.com/33818414/88252579-bc7d5c80-cce9-11ea-8502-c498fbfeb564.png)

