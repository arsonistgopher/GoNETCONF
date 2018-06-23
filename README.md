## Go-NETCONF pack

This pack was created over the weekend of June 23rd 2018 at the iNOG + RIPE Hackathon at DoWork in Dublin, Ireland.

Special thanks to the contributors (see pack.yaml), the venue (DoWork), RIPE and the organisers.

#### Intro

### Installation

### Usage

#### Actions
The following actions are supported.

- get_netconf

parameters

name  | type   |  description | required
--|---|--
target_ip  | string  |  IP Address of the target device | true
transport  | string  | transport mechanism to be used (ssh/direct) Default: ssh | true
port  |  Port which will be used for the netconf call |  Default: 22 | true
envelope  | string  |  Netconf data envelope | true
username  | string  |  Login user name to connect to the device | false
password  | string  |  Login password to connect to the device | false
ssh_key  |  string |  Path to a ssh_key used to authenticated | false





### Notes

### Contributing


### Any other business...
