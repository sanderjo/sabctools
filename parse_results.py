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

# find the CPU this python script is running on, and print it
import platform
print(f"Running on CPU: {platform.processor()}")

