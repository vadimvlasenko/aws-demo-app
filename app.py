#!/usr/bin/env python3
import os
import aws_cdk as cdk
from hello_api.api_stack import ApiStack

app = cdk.App()

ApiStack(app, "HelloApiStack")

app.synth()
