# RabbitMQ in Action Examples #


## Requirements ##

### Python Examples ###

* Python 2.6 or newer
* [Pika](https://github.com/pika/pika)

## Running the Examples: Python ##

### 3.2.2 Alerting Framework ###

_Requirements:_

* RabbitMQ server (2.6.1 or later) running on localhost.
* RabbitMQ user needed:
	* Username: alert\_user
	* Password: alertme
	* Permissions: read,write,config

_Running the Consumer:_  __python 3.2.2\_alert\_consumer.py__

_Running the Producer:_ __python 3.2.2\_alert\_producer.py -r ROUTING\_KEY -m MESSAGE__


### 3.3.3 RPC Example ###

_Requirements:_

* RabbitMQ server (2.6.1 or later) running on localhost.
* RabbitMQ user needed:
	* Username: rpc\_user
	* Password: rpcme
	* Permissions: read,write,config


_Running the Server:_ __python 3.3.3\_rpc\_server.py__
_Running the Client:_ __python 3.3.3\_rpc\_server.py__


## Note to contributors ##

**BY CONTRIBUTING TO THE RABBITMQ IN ACTION SOURCE CODE REPOSITORY YOU AGREE TO LICENSE YOUR CONTRIBUTION UNDER THE TERMS OF THE BSD LICENSE AS SPECIFIED IN THE 'LICENSE.md' FILE IN THIS DIRECTORY.**

