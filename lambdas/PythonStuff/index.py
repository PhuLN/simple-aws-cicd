# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def handler(event, context):
   event['input'] = {
     **event['input'],
     "pythonProperty": "Added a new property via the Python Lambda"
   };
   
   return event['input']
