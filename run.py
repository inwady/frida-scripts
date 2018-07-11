#!/usr/bin/python

import sys
import frida 
import time

def print_message(a, b):
    print(a)
    print(b)

if (len(sys.argv) < 3):
    exit("bad args")

package_name = sys.argv[1]
script_file = sys.argv[2]

print("Try to connect to device...")
device = frida.get_usb_device()

print("Start package...")
pid = device.spawn([package_name])
device.resume(pid)

# time.sleep(1) # Java perform

session = device.attach(pid)

with open(script_file) as f:
    script = session.create_script(f.read())

script.on("message", print_message)
script.load()

sys.stdin.read()
