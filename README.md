# junos-multiprocessing-config-collector

This wonderfully named repo houses code for collecting configuration from multiple Juniper (Junos) network devices using Python's multiprocessing library. The real purpose is to serve as boiler-plate code for multiprocessed command execution

#### Usage
```
1. Modify credentials.txt (new-line delimited to contain username and password)
2. Modify targets.txt with the IP addresses / hostnames of the target devices
3. python main.py
```