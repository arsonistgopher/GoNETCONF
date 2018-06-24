## Go-NETCONF pack

This pack was created over the weekend of June 23rd 2018 at the iNOG + RIPE Hackathon at DoWork in Dublin, Ireland.

Special thanks to the contributors (see pack.yaml), the venue (DoWork), RIPE and the organisers.

#### Intro

### Installation
The gonetconf pack can be installed from the command line of the stackstom server

Installation from command line:
```
st2 pack install git@github.com:ripe-stackstorm/GoNETCONF.git
```

### Usage
The Stacksorm Pack comes with 2 actions which can directly be used in any workflow. Example workflows are provided.

#### Workflows
The following workflows are provided as examples.

##### gonetconf.getworkflow
The workflow will take a Netconf envelope, either as a file a string and will perform a operational netconf querie against the desired device. The workflow will return a json string with the results.

_Workflow Requirements_

The workflow requires the stackstorm-xml pack to be installed. (https://github.com/StackStorm-Exchange/stackstorm-xml)

_Workflow Parameters_

|name  | type   |  description | required |
|--|---|--
|targethost  | string  |  IP Address/FQDN of target device | true|
|transport  | string/enum  | transport mechanism to be used (ssh/direct) Default: ssh (Not Implemented) | true |
|port  |  Port which will be used for the netconf call |  Default: 22 | true |
|envelope  | string  |  Netconf data envelope string | false |
|envelope_file   | string  | path to file which contains a Netconf envelope  | false  |
|username  | string  |  Login user name to connect to the device | false |
|password  | string  |  Login password to connect to the device | false |
|ssh_key  |  string |  Path to a ssh_key used to authenticated | false |
|clean_output   | boolean  | Should the return output from the device be cleaned from whitspaces and line returns (Default: true)  | false  |

_Workflow Steps_
- get_netconf_information
- strip_new_line_chars
- convert_xml_to_json

_Example_
Example:
Envelope:
```
<get-system-information/>
```

Result:
```
"result": {
  "system-information": {
    "host-name": "myhostname",
    "hardware-model": "vmx",
    "serial-number": "myserialnumber",
    "os-name": "junos",
    "os-version": "18.1R1.9"
  }
```

##### gonetconf.setworkflow
The workflow will take a Netconf envelope, either as a file a string and will perform a netconf configuration against the desired device. The workflow will return a json string with the results.

_Workflow Requirements_

The workflow requires the stackstorm-xml pack to be installed. (https://github.com/StackStorm-Exchange/stackstorm-xml)

_Workflow Parameters_

|name  | type   |  description | required |
|--|---|--
|targethost  | string  |  IP Address/FQDN of target device | true|
|transport  | string/enum  | transport mechanism to be used (ssh/direct) Default: ssh (Not Implemented) | true |
|port  |  Port which will be used for the netconf call |  Default: 22 | true |
|envelope  | string  |  Netconf data envelope string | false |
|envelope_file   | string  | path to file which contains a Netconf envelope  | false  |
|username  | string  |  Login user name to connect to the device | false |
|password  | string  |  Login password to connect to the device | false |
|ssh_key  |  string |  Path to a ssh_key used to authenticated | false |
|clean_output   | boolean  | Should the return output from the device be cleaned from whitspaces and line returns (Default: true)  | false  |
|lock   | boolean  |  Should the datastore be locked |  false |
|datastore   | string/enum  | Name of the datastore to be used (startup,config,candidate)  |  true |

_Workflow Steps_
- set_netconf_information
- strip_new_line_chars
- convert_xml_to_json


#### Actions
The following actions are supported.

##### get_netconf

_parameters_

|name  | type   |  description | required |
|--|---|--
|targethost  | string  |  IP Address/FQDN of target device | true|
|transport  | string/enum  | transport mechanism to be used (ssh/direct) Default: ssh (Not Implemented) | true |
|port  |  Port which will be used for the netconf call |  Default: 22 | true |
|envelope  | string  |  Netconf data envelope string | false |
|envelope_file   | string  | path to file which contains a Netconf envelope  | false  |
|username  | string  |  Login user name to connect to the device | false |
|password  | string  |  Login password to connect to the device | false |
|ssh_key  |  string |  Path to a ssh_key used to authenticated | false |
|clean_output   | boolean  | Should the return output from the device be cleaned from whitspaces and line returns (Default: true)  | false  |

Example:
Envelope:
```
<get-system-information/>
```
Result:
```
<system-information>
<hardware-model>vmx</hardware-model>
<os-name>junos</os-name>
<os-version>18.1R1.9</os-version>
<serial-number>myserialnumber</serial-number>
<host-name>myhostname</host-name>
</system-information>
```

- set_netconf

|name  | type   |  description | required |
|--|---|--
|targethost  | string  |  IP Address/FQDN of target device | true|
|transport  | string/enum  | transport mechanism to be used (ssh/direct) Default: ssh (Not Implemented) | true |
|port  |  Port which will be used for the netconf call |  Default: 22 | true |
|envelope  | string  |  Netconf data envelope string | false |
|envelope_file   | string  | path to file which contains a Netconf envelope  | false  |
|username  | string  |  Login user name to connect to the device | false |
|password  | string  |  Login password to connect to the device | false |
|ssh_key  |  string |  Path to a ssh_key used to authenticated | false |
|clean_output   | boolean  | Should the return output from the device be cleaned from whitspaces and line returns (Default: true)  | false  |
|lock   | boolean  |  Should the datastore be locked |  false |
|datastore   | string/enum  | Name of the datastore to be used (startup,config,candidate)  |  true |

### Notes
The examples folder contains example files for netconf envlope files which can be used with envelope_file paramter

### Contributing


### Any other business...
