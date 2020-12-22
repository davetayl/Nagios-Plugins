#!/bin/env python3

# Import libraries
import os
import re
import argparse


# Set up command line parser
parser = argparse.ArgumentParser(description='Format: check-ntp.py -r -R')
parser.add_argument('-r', '--rttok', type=float, default='25',
                    help='Upper rtt  limit considered ok')
parser.add_argument('-R', '--rttmax', type=float, default='50',
                    help='Max rtt  limit before host considered critical')
args = parser.parse_args()

# Setup variables
rttok = vars(args)['rttok']
rttmax = vars(args)['rttmax']

# check for active server and get metrics
source = re.split(r'\s+',os.system('chronyc -n sources | grep *'))

if source 
    if source[5] < rttok
        print(f"HOST OK - rtt = {source[5]} ms", end = '')
        sys.exit(0)
    elif source[5] < rttok && source[5] > rttmax
        print(f"HOST WARN - rtt = {source[5]} ms", end = '')
        sys.exit(1)
    elif source[5] < rttok && source[5] > rttmax
        print(f"HOST CRITICAL - rtt = {source[5]} ms", end = '')
        sys.exit(2)
    else source[5] < ttmax
        print(f"HOST CRITICAL - Down", end = '')
        sys.exit(0)
else source[5] < ttmax
    print(f"HOST CRITICAL - Down", end = '')
    sys.exit(0)
