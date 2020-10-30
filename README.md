Python client for the tp-link hs100, hs110 and hs200 wifi plug
============

I (Nealefelaen) didn't like how netcat was working with the response from my hs110 so I rewrote the minimum of the script in Python (no check, toggle, or argument checking).

Original bash script at: https://github.com/ggeorgovassilis/linuxscripts/tree/master/tp-link-hs100-smartplug

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
hs100.py 192.168.1.20 9999 status
```

Print power consumption (tested and working with my (Nealefelaen's) hs110):
```sh
hs100.py 192.168.1.20 9999 emeter
```

Print watt hours for recorded days:
```sh
hs100.py 192.168.1.20 9999 daystat_wh
```

Print minutes uptime for recorded days:
```sh
hs100.py 192.168.1.20 9999 daystat_time
```

... work in progress, the Kasa app also has weekly and monthly summaries as well as current/average vs total - probably more commands to find :)

Some commands that I found that I'm not sure what they do:

daystat (gives me an empty list in the same format as daystat_wh)

dayhistory (gives me an empty list in the same format as daystat_time)

realtime2 (probably just a duplicate of emeter)
