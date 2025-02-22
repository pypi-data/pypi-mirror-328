#!/usr/bin/env python3
# Template Author: NhanDD <hp.duongducnhan@gmail.com>
#
# THIS CODE REQUIRED Lib cmk_tools >= 2.0.6
#
# enable if you want to use libs
# require install extra libs: snmp, requests
# import netsnmp
# import re
# import ast
import json
import traceback
import sys
from cmk_tools import (
    setup_log, 
    make_request_v2,
    terminate_check,
    detect_is_test_host,
    set_plugin_id,

    # if you want to use more functions, you could import here

    # -- this is elk client and search function, you could use it to search data from elk
    #  _____ _     _  __   ____ _ _            _   
    # | ____| |   | |/ /  / ___| (_) ___ _ __ | |_ 
    # |  _| | |   | ' /  | |   | | |/ _ \ '_ \| __|
    # | |___| |___| . \  | |___| | |  __/ | | | |_ 
    # |_____|_____|_|\_\  \____|_|_|\___|_| |_|\__|
    # new_elk_client,
    # elk_search,

    # -- this is snmp get function, you could use it to get data from snmp
    #  ____  _   _ __  __ ____     ____ _ _            _   
    # / ___|| \ | |  \/  |  _ \   / ___| (_) ___ _ __ | |_ 
    # \___ \|  \| | |\/| | |_) | | |   | | |/ _ \ '_ \| __|
    #  ___) | |\  | |  | |  __/  | |___| | |  __/ | | | |_ 
    # |____/|_| \_|_|  |_|_|      \____|_|_|\___|_| |_|\__|
    # snmp_get,
)
# from datetime import datetime, timezone
from pathlib import Path
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# -----------------------------------------   
#   DO NOT MODIFY BELLOW CONSTANTS
#   you could add more constants if you need
# -----------------------------------------   
DEBUG = "DEBUG"
OK = "OK"
WARN = "WARN"
WARNING = "WARNING"
CRITICAL = "CRITICAL"
ERROR = "ERROR"
UNKNOWN = "UNKNOWN"


# -----------------------------------------   
# create logger, DO NOT MODIFY logger and log function
logger = setup_log("{{cookiecutter.agent_id}}")
def log(msg, **kwargs):  
    # shortcut log, you could use directly logger
    logger.info(msg, extra={'service_name': '{{cookiecutter.agent_id}}',})

def run():
    # -----------------------------------------   
    #   DO NOT MODIFY THIS FUNCTION
    # -----------------------------------------    
    plugin_id = "{{cookiecutter.agent_id}}"
    set_plugin_id(plugin_id)

    # set default value for arguments
    data = None
    ip = ''
    hostname = ''
    community = ''
    scctestenable = False
    scctestdomain = ''

    try:
        args = sys.argv[1:]
        while args:
            section = args.pop(0)
            if section == '--data':
                formatted_json = args.pop(0).replace("'", '"')
                data = json.loads(formatted_json)
            if section == '--ip':
                ip = str(args.pop(0))
            if section == '--hostname':
                hostname = str(args.pop(0))
            if section == '--community':
                community = str(args.pop(0))
                if community == '$_HOSTSNMPCOMMUNITY$':
                    community = None
            if section == '--scctestenable':
                scctestenable = str(args.pop(0))
            if section == '--scctestdomain':
                scctestdomain = str(args.pop(0))

        if scctestenable and scctestdomain:
            detect_is_test_host(scctestenable, scctestdomain)

    except Exception as e:
        terminate_check(UNKNOWN, f"Error when parse arguments with error: {e}")
    
    if not data:
        terminate_check(UNKNOWN, "Missing data argument")
    if not ip:
        terminate_check(UNKNOWN, "Missing ip argument")
    
    # run agent 
    try:
        run_active_check(data, ip, community, hostname=hostname)
    except Exception as e:
        terminate_check(UNKNOWN, f"Error when run active check with error: {e} ---> {traceback.format_exc(10)}")
    

# ----------------------------------------- 
#   Your code begin here, entry point is run_active_check function
#   You could define other function to support run_active_check function
#   DO NOT MODIFY ABOVE, If you need other id, create new plugin template!
# -----------------------------------------        
def run_active_check(data, host_ip, snmp_community, **kwargs):
    # 
    # YOUR CODE HERE
    #
    return code_sample(data, host_ip, snmp_community, **kwargs)

def code_sample(data, host_ip, snmp_community, **kwargs):
    log(f"run check with data {data} for host {host_ip} with community {snmp_community} and kwargs {kwargs}")
    must_name01 = 'sample01'
    must_name02 = 'sample02'
    count_01_range = (50, 150,)
    count_02_range = (190, 210,)

    result01 = make_request_v2(
        "http://42.119.16.154:8080/testcase/api/stage/sample01/", 
        method="GET", verify=False, 
        stage_id='1'
    )
    res01 = result01.json()
    count01 = res01.get('data', {}).get('count', 0)
    name01 = res01.get('data', {}).get('name','')

    result02 = make_request_v2(
        "http://42.119.16.154:8080/testcase/api/stage/sample02/", 
        method="GET", verify=False, 
        stage_id='2'
    )
    res02 = result02.json()
    count02 = 0
    name02 = ''
    for item in res02.get('data', []):
        key = item.get('key', '')
        value = item.get('value', 0)
        if key == 'name':
            name02 = value
        if key == 'count':
            count02 = value
    
    if name01 == must_name01 and name02 == must_name02 and count01 in range(*count_01_range) and count02 in range(*count_02_range):
        terminate_check(OK, f"All OK: Name01: {name01}, Name02: {name02}, Count01: {count01}, Count02: {count02}")
    
    if count01 in range(*count_01_range) and count02 in range(*count_02_range):
        terminate_check(WARNING, f"Count in range but name is wrong -> Name01: {name01} -> must be {must_name01}, Name02: {name02} -> must be {must_name02}")

    terminate_check(
        CRITICAL, 
        f"Count not in range -> Count01: {count01} -> must be in range {count_01_range}, Count02: {count02} -> must be in range {count_02_range} and Name01: {name01} -> must be {must_name01}, Name02: {name02} -> must be {must_name02}"
    )

if __name__ == '__main__':
    # ----------------------------------------- 
    #   DO NOT MODIFY
    # -----------------------------------------    
    run()
    # -----------------------------------------
