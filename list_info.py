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
        with p.open() as f:
            t = json.load(f)
            yaml.safe_dump(t, sys.stdout, allow_unicode=True)
            print()


if __name__ == "__main__":
    main()
