#!/bin/env python3

# Import libraries
import os
import re
import argparse


# Set up command line parser
parser = argparse.ArgumentParser(description='Format: check-ntp.py -r -R host')
parser.add_argument('-r', '--rttok', type=float, default='25',
                    help='Upper rtt  limit considered ok')
parser.add_argument('-R', '--rttmax', type=float, default='50',
                    help='Max rtt  limit before host considered critical')
args = parser.parse_args()

# Setup variables
rttok = vars(args)['rttok']
rttmax = vars(args)['rttmax']

## Pseudo code
# get list of configured servers and status
source = re.split(r'\s+',os.system('chronyc -n sources | grep *'))

# for for active server get metrics
# create dictionary based on metric list, split and remove blanc spaces
# check values for latency, jitter against arg values
# output status and latency
