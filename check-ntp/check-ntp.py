#!/bin/env python3

# Import libraries
import sys
import os
import re
import argparse


# Set up command line parser
parser = argparse.ArgumentParser(description='Format: check-ntp.py -r -R -h')
parser.add_argument('-r', '--rttok', type=float, default='25',
                    help='Upper rtt  limit considered ok')
parser.add_argument('-R', '--rttmax', type=float, default='50',
                    help='Max rtt  limit before host considered critical')
args = parser.parse_args()

# Setup variables
rttok = vars(args)['rttok']
rttmax = vars(args)['rttmax']

# check for active server and get metrics
source = re.split(r'\s+',str(os.popen('chronyc -n sources | grep \*').read()))
source = float(source[9].replace('ms',''))

if source != 0:
    if source < rttok:
        print(f"HOST OK - rtt = {source}ms")
        sys.exit(0)
    elif source > rttok and source < rttmax:
        print(f"HOST WARN - rtt = {source}ms")
        sys.exit(1)
    elif source > rttmax:
        print(f"HOST CRITICAL - rtt = {source}ms")
        sys.exit(2)
    else:
        print(f"HOST CRITICAL - Down")
        sys.exit(0)
else:
    print(f"HOST CRITICAL - Unknown")
    sys.exit(0)
