# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json

def handler(event, context):
   response = {
       "pythonProperty": "Added a new property via the Python Lambda"
   }

   event['input'] = response;
   
   return event['input']
