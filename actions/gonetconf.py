from __future__ import print_function
import argparse
import json
import sys

parser = argparse.ArgumentParser(description='Test interface modelling go module.')
parser.add_argument('-target_ip', required=True,
                   help='')
parser.add_argument('-transport', 
                   help='')
parser.add_argument('-envelope',
                   help='')
parser.add_argument('-username', 
                   help='')
parser.add_argument('-password', 
                   help='')
parser.add_argument('-ssh_key', 
                   help='')
parser.add_argument('-port', type=int, 
                   help='')
args = parser.parse_args()
arg_dictionary = vars(args)
print(json.dumps(arg_dictionary), file=sys.stdout)
sys.exit(0)