#!/usr/bin/env python3
import sys


def parseresults(input):
    for line in input:
        if line.startswith("test_sabctools_decode"):
            print("SABCTOOLS DECODE BENCHMARK:")
            ops = line.split()[-4].split('.')[0].replace(',', '')
            print(f"Operations: {ops}, thus {int(ops)*0.39} MB/s")
        elif line.startswith("test_python_decode"):
            print("PYTHON DECODE BENCHMARK:")
            ops = line.split()[-4].split('.')[0].replace(',', '')
            print(f"Operations: {ops}, thus {int(ops)*0.39} MB/s")



try:
    resultsfile = sys.argv[1]
    with open(resultsfile, "r") as f:
        parseresults(f)
except:
    print("No file provided, reading from stdin...")
    parseresults(sys.stdin)


import platform
import subprocess
import os

def get_processor_name():
    # Method 1: Standard library
    proc = platform.processor()
    if proc:
        return proc

    # Method 2: Windows Registry/Environment
    if platform.system() == "Windows":
        return os.environ.get('PROCESSOR_IDENTIFIER', 'Unknown Windows CPU')

    # Method 3: Linux (reading /proc/cpuinfo)
    if platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep 'model name' | uniq"
        try:
            line = subprocess.check_output(command, shell=True).decode().strip()
            return line.split(":")[1].strip()
        except:
            pass

    # Method 4: macOS
    if platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        try:
            return subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']).decode().strip()
        except:
            pass

    return "CPU name not found"

print(f"Processor: {get_processor_name()}")
print(f"Architecture: {platform.machine()}")

