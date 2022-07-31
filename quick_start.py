#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/31 15:24
# @Author  : tolatolatop
# @File    : quick_start.py
# Download the helper library from https://www.twilio.com/docs/python/install
import os
import pathlib
import sys

import yaml
from twilio.rest import Client


def read_config(path: pathlib.Path):
    with path.open('r') as f:
        conf = yaml.safe_load(f)
    return conf


config = read_config('./config.yaml')

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config['TWILIO_ACCOUNT_SID']
auth_token = config['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_=sys.argv[1],
    to=sys.argv[2]
)

print(message.sid)
