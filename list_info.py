#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/31 16:21
# @Author  : tolatolatop
# @File    : list_info.py
import json
import pathlib
import sys

import yaml


def main():
    for p in pathlib.Path(sys.argv[1]).glob('*.json'):
        b = {}
        with p.open() as f:
            t = json.load(f)['address']
            b['Temporary_mail'] = t['Temporary_mail']
            b['Full_Name'] = t['Full_Name']
            b['Birthday'] = t['Birthday']
            b['Password'] = t['Password']
            b['Address'] = t['Address']
            b['City'] = t['City']
            b['Zip_Code'] = t['Zip_Code']

            yaml.safe_dump(b, sys.stdout, allow_unicode=True)
            print()


if __name__ == "__main__":
    main()
