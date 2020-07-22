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
- When the shell code ends, check the **created txt and JSON files**.


2. Run **findConvergence.py** in the terminal command.
```sh
./findConvergence.py
```
- This python code analyzes a txt file and outputs the **index and offset of the converged section.**


3. Run **jsonToCsv.py** in the terminal command.
- This python code converts log files output in JSON format to **csv files**.
```sh
./jsonTocsv.py
```

4. Run **csv_Visualization.ipynb** in the jupyter-notebook
- This file **visualizes the data** via csv file.
 ```sh
 jupyter-notebook
 ```




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



