#!/bin/python

import sys
import base64
import socket
import json

# encoded (the reverse of decode) commands to send to the plug

# encoded {"system":{"set_relay_state":{"state":1}}}
payload_on="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog=="

# encoded {"system":{"set_relay_state":{"state":0}}}
payload_off="AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow=="

# encoded { "system":{ "get_sysinfo":null } }
payload_query="AAAAI9Dw0qHYq9+61/XPtJS20bTAn+yV5o/hh+jK8J7rh+vLtpbr"

# the encoded request { "emeter":{ "get_realtime":null } }
payload_emeter="AAAAJNDw0rfav8uu3P7Ev5+92r/LlOaD4o76k/6buYPtmPSYuMXlmA=="

payload_daystat="AAAAbtDykf6Q5IH5ja+V7sy/0KXXtNHzyevf6Yi82O3Vt5qsnqmQvYm6iOvGp8Lww+6Luou+3e+L6dHi1+PBvJCy17rfq868nqTf/Zr/i9Sw0ajbr866mKLZ+5b5l+OLqZOqhqTduNmribOBsYOzzrPO"

payload_daystat_wh="AAAAb9Dykf6Q5IH5ja+V7sy/0KXXtNHzyevf6Yi82O3Vt5qsnqmQvYm6iOvGp8Lww+6Luou+3e+L6dHi1+PBvJCy17rfq868nqTf/Zr/i9Sw0ajbr866mKLZ+5b5l+OLqZOikr6c5YDhk7GLuYm7i/aL9g=="

payload_emeter2="AAAAWtDykf6Q5IH5ja+V7sy/0KXXtNHzyevf6Yi82O3Vt5qsnqmQvYm6iOvGp8Lww+6Luou+3e+L6dHi1+PBvJCy17rfq868nqTf/Zr/i9Smw6LOutO+2/nDuMW4xQ=="

payload_schedule_getdaystat="AAAAcNDykf6Q5IH5ja+V7sy/0KXXtNHzyevf6Yi82O3Vt5qsnqmQvYm6iOvGp8Lww+6Luou+3e+L6dHi1+PBvJCywaLKr8u+0reVr9T2kfSA37vao9CkxbGTqdLwnfKc6ICimKGNr9az0qCCuIq6iLjFuMU="

payload_daystat_time="AAAAcdDykf6Q5IH5ja+V7sy/0KXXtNHzyevf6Yi82O3Vt5qsnqmQvYm6iOvGp8Lww+6Luou+3e+L6dHi1+PBvJCywaLKr8u+0reVr9T2kfSA37vao9CkxbGTqdLwnfKc6ICimKmZtZfui+qYuoCygrCA/YD9"

payload_realtime2="AAAAWtDykf6Q5IH5ja+V7sy/0KXXtNHzyevf6Yi82O3Vt5qsnqmQvYm6iOvGp8Lww+6Luou+3e+L6dHi1+PBvJCy17rfq868nqTf/Zr/i9Smw6LOutO+2/nDuMW4xQ=="

ip=sys.argv[1]
port=int(sys.argv[2])
cmd=sys.argv[3]

if cmd == 'on':
    data=base64.b64decode(payload_on)
elif cmd == 'off':
    data=base64.b64decode(payload_off)
elif cmd == 'status':
    data=base64.b64decode(payload_query)
elif cmd == 'emeter':
    data=base64.b64decode(payload_emeter)
elif cmd == 'daystat_wh':
    data=base64.b64decode(payload_daystat_wh)
elif cmd == 'daystat_time':
    data=base64.b64decode(payload_daystat_time)
elif cmd == 'dayhistory':
    data=base64.b64decode(payload_dayhistory)
elif cmd == 'emeter2':
    data=base64.b64decode(payload_emeter2)
elif cmd == 'realtime2':
    data=base64.b64decode(payload_realtime2)
elif cmd == 'unknown':
    data=base64.b64decode(payload_unknown)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))
s.send(data)
s.recv(4)
result = s.recv(1024)
res=""
code=171
for x in result:
    res+= chr(x ^ code)
    code=x
print(res)
