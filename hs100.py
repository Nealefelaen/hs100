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
