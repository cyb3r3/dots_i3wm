#!/usr/bin/env python3
import sys
import json
import subprocess

def get_caps():
    try:
        out = subprocess.check_output(['xset', 'q']).decode()
        for line in out.splitlines():
            if 'Caps Lock' in line:
                if 'on' in line.split('Caps Lock')[1][:10]:
                    return {"full_text": "[CAPS]", "color": "#FF5555", "name": "caps", "markup": "none"}
        return {"full_text": " ::OFF::", "color": "#4A4654", "name": "caps", "markup": "none"}
    except:
        return {"full_text": "::OFF::", "name": "caps", "markup": "none"}
sys.stdout.write(sys.stdin.readline())
sys.stdout.flush()
sys.stdin.readline()
sys.stdout.write("[\n")
sys.stdout.flush()

first = True
for line in sys.stdin:
    line = line.strip().lstrip(',')
    if not line:
        continue
    try:
        blocks = json.loads(line)
        blocks.insert(0, get_caps())
        prefix = "" if first else ","
        sys.stdout.write(prefix + json.dumps(blocks) + "\n")
        sys.stdout.flush()
        first = False
    except:
        continue
