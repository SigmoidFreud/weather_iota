# weather_iota - Python package

The IOTA Weather Node is a Weather Node built with a [Raspberry Pi](https://www.raspberrypi.org/) and the add-on board  [Sense HAT](https://www.raspberrypi.org/products/sense-hat/).
The Weather Node send and receive Data over the new [IOTA Protocol](https://www.iotatoken.com/).

## What I need to run an weather_iota instance?

required:
- [ ] Install the latest IOTA release from : [IOTA Node](https://github.com/IOTAledger/iota-gui-beta/releases)
- [ ] Install the latest iota python package [iota](https://github.com/necropaz/iota)
- [ ] the python package sys, json, urllib2 and os are also required

for more fun:
- [ ] [Raspberry Pi](https://www.raspberrypi.org/)
- [ ] microSD card with installed [Ubuntu MATE 16.04 LTS](https://ubuntu-mate.org/download/)
- [ ] Raspberry Pi [Sense HAT](https://www.raspberrypi.org/products/sense-hat/)
- [ ] Sense HAT python [package](https://pypi.python.org/pypi/sense-hat)


## Installation

To install the package it is very easy if you have installed pip.

```ShellSession
$ sudo pip install weather_iota
```

## weathernode
The IOTA Weather Node waiting until a client send a transaction with >0 IOTAs and a message.
With the message the client tell the node what is his request and an address on which the node can send his answer.
So can be send a command is arrived over the IOTA Protocol.
After this he read the Weather info from the Sense HAT and send them back or just show a promotion on his 8x8 LED Matrix.

### running instance
- First you have to import the package 
```Python
from weather_iota import weathernode
```

- Now you can run an instance very easy
```Python
node=weathernode("HIERCOMESMYSEED", temperature=100, humidity= 54, pressure=1024, senseHAT=false)
node.run()
```

### Testing
You can run this script to test the weather node:
```Python
import sys
import json
import time
import os
from weather_iota import weathernode

seed=raw_input("Enter the seed of the IOTA Weather Node? ")

weather=weathernode(seed, temperature="32",humidity="50",pressure="1013", senseHAT=False)
weather.run()
print("End Iota Weather Node!")
```

### weathernode class

#### `weathernode( seed, temperature=None, humidity=None, pressure=None, senseHAT=True)`

Send a message to a specified Adress.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

#### `run()`

Send a message to a specified Address.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

#### `execute(jsonData)`

Send a request to the IOTA Node and return the answer.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`command` | string | Yes | The command which will made the request.
`return` |`jsonData` | string | Yes | The answer from the request in JSON.

#### `readWeather()`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`return` |`transaction` | string | Yes | Hash of the last transaction.

#### `scrollText(message)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`transaction` | string | Yes | Hash of the transaction from which you wanna read the sender address.
`return` |`address` | string | Yes | Sender address of the transaction.

## weather client


### running instance
- First you have to import the package 
```Python
from weather_iota import weatherclient
```

- Now you can run an instance very easy
```Python
client=weatherclient("HIERCOMESMYSEED", "THEADDRESSOFTHEIOTAWEATHERNODE")
client.requestWeather()
client.sendPromotion("Here comes my promotion!")
```
### Testing
You can run this script to test the weather client. There is a test instance running on a VPS Server you can use this address:
```Python
import sys
import json
import time
import os
from weather_iota import weatherclient

address=raw_input("The address of the Weather Node? ")
seed=raw_input("The seed of you Weather Client? ")
char=raw_input("If you will send a weather request tip w, if you wanna send a promotion tip p.? [w/p]? ")

client=weatherclient(seed, address)

if char=='w':
	client.requestWeather()

elif char=='p':
	message=raw_input("What for a promotion you wanna send? ")
	client.sendPromotion(message)

else:
	print("Your Input is not [r/p]")
```

### weatherclient class

#### `weatherclient( seed, address)`

Send a message to a specified Adress.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

#### `requestWeather()`

Send a message to a specified Address.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`seed` | string | Yes | 81-char encoded string which contains the accounts seed. The seed must be correctly encoded: only uppercase latin letters and 9’s. No other characters are allowed.
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`input` |`message` | string | Yes | The message which added to the transation.
`input` |`value` | string | Yes | string the quantity of IOTA’s which should be transferred.

#### `sendPromotion(message)`

Send a request to the IOTA Node and return the answer.

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`command` | string | Yes | The command which will made the request.
`return` |`jsonData` | string | Yes | The answer from the request in JSON.

#### `execute(jsonData)`

Direction |Parameters | Type | Required | Description
------------ |------------ | ------------- | ------------- | -------------
`input` |`address` | string | Yes | 81-char long address of the recipient of a transaction.
`return` |`transaction` | string | Yes | Hash of the last transaction.


