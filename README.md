# Introduction
This files used the Precision Time Protocol(PTP) according to IEEE standard 1588 for Linux.

It contains log files that are generated at a specified time and analyzed and visualized.

# Environment
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

![run_1](https://user-images.githubusercontent.com/33818414/88355198-982f8780-cd9e-11ea-98a2-49bd8e57a874.png)


- When the ptp4l service ends, Input the file name to convert JSON file to csv


![run_2](https://user-images.githubusercontent.com/33818414/88355201-9a91e180-cd9e-11ea-8b92-69e487946bf3.png)


- When the file name is entered, check the **created txt and JSON files**.
- A csv file is created
- A txt file is read to output the convergence **index and offset**

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


## scatter_Visualization.ipynb
This file visualizes the data.


### Result
![offset_during5min](https://user-images.githubusercontent.com/33818414/88353819-e7bf8480-cd99-11ea-9e49-eb44e81a3b55.png)



#### 0 - 1 min
![offset_0_1min](https://user-images.githubusercontent.com/33818414/88353830-ebeba200-cd99-11ea-98f6-d5f77fd65f1a.png)


#### 1 - 2 min
![offset_1_2min](https://user-images.githubusercontent.com/33818414/88353832-ee4dfc00-cd99-11ea-9a1a-2081245a0c1e.png)


#### 90 - END
![offset_2min_END](https://user-images.githubusercontent.com/33818414/88353834-f0b05600-cd99-11ea-8500-d20fe421af10.png)


