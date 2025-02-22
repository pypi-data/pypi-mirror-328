#!/usr/bin/env python3
# Template Author: NhanDD <hp.duongducnhan@gmail.com>

"""
Simple Packer and (later) unpacker for MKP Files
MKP is the Package format for Check_MK
"""
import os
from cmk_tools import pack_mkp

#
# DO NOT CHANGE THIS FILE CONTENT
#
base_path = os.getcwd()
package_name = "{{cookiecutter.agent_id}}"
checks_file = 'agent_{{cookiecutter.agent_id}}.py'
lib_file = 'agent_{{cookiecutter.agent_id}}.py'
wato_file = '{{cookiecutter.agent_id}}_register.py'


#
# DO NOT CHANGE THIS FILE CONTENT
#
if __name__ == "__main__":
    pack_mkp(
        package_name=package_name,
        checks_file=checks_file,
        lib_file=lib_file,
        wato_file=wato_file,
        base_path=base_path
    )
#
# DO NOT CHANGE THIS FILE CONTENT
#