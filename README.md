Python client for the tp-link hs100, hs110 and hs200 wifi plug
============

Python script to connect over TCP/IP to an hs100, hs103, hs110, hs200 smart plugs, switch it on and off and query status information. You'll need the IP address and port (was 9999 in my tests) and a command, e.g.:

Switch plug on:
```sh
hs100.py 192.168.1.20 9999 on
```

Switch plug off:
```sh
hs100.py 192.168.1.20 9999 off
```

Print plug system status:
```sh
hs100.sh 192.168.1.20 9999 status
```

Print power consumption (tested and working with my (Nealefelaen's) hs110):
```sh
hs100.sh 192.168.1.20 9999 emeter
