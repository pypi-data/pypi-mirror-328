# -*- coding: utf-8 -*-

"""Entry point of my coca tools
"""
import os
import sys
import traceback

from cookiecutter.main import cookiecutter

__version__ = '2.0.4'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE_PATH, 'cookiecutter_templates')


def welcome():
    """Say welcome to users"""
    print(f'I am , welcome to CheckMK Plugin Maker version {__version__}')


def create_cmk_active_check():
    template_path = os.path.join(TEMPLATE_PATH, 'cmk_active_check')
    try:
        cookiecutter(template_path)
    except Exception as e:  # pylint: disable=broad-except
        print('Error creating cmk_active_check', e)
        print(traceback.format_exc())
        return 1
    return 0
