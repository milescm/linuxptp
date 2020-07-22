# Introduction
This software is an implementation of the Precision Time Protocol(PTP) according to IEEE standard 1588 for Linux.

# Envorinment
Master OS : Ubuntu20.04LTS
Slave OS : Ubuntu18.04LTS

# Precondition
The master computer must always be running.

# How to Use
1. Run 'run.sh' in the terminal commmand.
2. When the shell code ends, check the created TXT and JSON files.
3. 



## run.sh
This shell code runs on the slave. This program runs the 'ptp4l' service for 5min and stops it.
The log of the service is saved as a TXT file and a JSON file through redirection.
The JSON file has TIMESTAMP, but the TXT file has no time variable.


