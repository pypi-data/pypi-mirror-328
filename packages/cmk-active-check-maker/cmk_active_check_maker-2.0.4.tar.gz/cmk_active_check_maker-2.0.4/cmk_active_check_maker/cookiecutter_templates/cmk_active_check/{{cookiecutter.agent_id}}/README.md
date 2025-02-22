# Checkmk Active Check Plugin - {{cookiecutter.agent_id}}

## Overview

This Checkmk plugin provides an **Active Check** that monitors specific services or conditions in your infrastructure.  
The plugin is packaged as a `.mkp` file, which can be installed in Checkmk to extend its monitoring capabilities.  
The plugin allows for real-time checks on the specified services by running custom scripts or commands and integrates with Checkmk's monitoring system.

## Features

- Executes custom scripts for active checks.
- Fully integrates with Checkmk.
- Configurable thresholds and parameters.
- Generates alert and performance data.

## Requirements

- Checkmk version: `>= 2.1.1`
- Python version: `>= 3.12`
- Lib: cmk-tools >= 2.0.5, < 3
- Access to the system/service being monitored.

## Installation

### Step 1: Install the Plugin

1. Prepare python and poetry 
2. Install the requirements:

    ```bash
    poetry install && poetry shell 
    ```


## Development

### Step 1: Configure input parameters

1. Target file **run_check.py**
2. Update parameters:

    ```text
    HOST_IP = 'your-device'
    SNMP_COMMUNITY = 'snmp-community'
    SAMPLE_DATA = 'should be the dictionary contains data for active check'
    OTHER_KWARGS = 'should be the dictionary contains extra data, optionals'
    ```


### Step 2: Run the check for testing

1. Using python command
    ```bash
    poetry run python run_check.py
    ```



## Using `make_request_v2`

Here is an example of how to use the `make_request_v2` function:

```python
from cmk_tools import make_request_v2

response = make_request_v2(
    url='https://api.example.com/data',
    method='GET',
    headers={'Authorization': 'Bearer YOUR_TOKEN'},
    params={'key': 'value'},
    data={'key': 'value'},
    stage_id='unique-id',
)
print(response.json())
```

## Using `es_client`

Here is an example of how to use the `es_client` function:

```python
from cmk_tools import new_elk_client, elk_search

es_client = new_elk_client('host', 'port', 'username', 'password')
body = {"query": {}, "sort": []}
search_res = elk_search(
    es_client, 
    'index', body, 
    with_scroll=False, 
    stage_id='unique-id'
)

# search_res should be an arrays of inner hits
print(search_res)
```

Here is an example of how to use the `es_client` search `with scroll` for get many data:

```python
from cmk_tools import new_elk_client, elk_search

es_client = new_elk_client('host', 'port', 'username', 'password')
body = {"query": {}, "sort": []}
search_res = elk_search(
    es_client, 
    'index', body, 
    with_scroll=True, 
    stage_id='unique-id'
)

# search_res should be an arrays of inner hits
print(search_res)
```


## Using `snmp_get`

Here is an example of how to use the `snmp_get` function:

```python
from cmk_tools import snmp_get

data = netsnmp.VarList(
    '....',
)
result = snmp_get(
    host='192.168.1.1',
    community='public',
    data=data,
    stage_id='unique-id'
)

print(result)
```

## Documents
1. Add/Update your documents to /docs