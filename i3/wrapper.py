#!/usr/bin/env python3

#ALL OF THIS IS MADE BY CLUADE, THIS IS A WORK IN PROGRESS
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

def get_bluetooth():
    try:
        result = subprocess.run(
            ["bluetoothctl", "show"],
            capture_output=True, text=True
        )
        powered = "Powered: yes" in result.stdout

        if not powered:
            return {"name": "bluetooth", "full_text": ":: OFF::", "color": "#666666", "markup": "none"}

        devices = subprocess.run(
            ["bluetoothctl", "info"],
            capture_output=True, text=True
        )
        if "Connected: yes" in devices.stdout:
            for line in devices.stdout.splitlines():
                if "Name:" in line:
                    name = line.split("Name:")[1].strip()
                    return {"name": "bluetooth", "full_text": f"[ {name}]", "color": "#AFA7C7", "markup": "none"}
            return {"name": "bluetooth", "full_text": " connected", "color": "#AFA7C7", "markup": "none"}

        return {"name": "bluetooth", "full_text": ":: ON::", "color": "#AFA7C7", "markup": "none"}

    except FileNotFoundError:
        return None

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
        bt = get_bluetooth()
        if bt:
            blocks.insert(1, bt)
        prefix = "" if first else ","
        sys.stdout.write(prefix + json.dumps(blocks) + "\n")
        sys.stdout.flush()
        first = False
    except:
        continue
