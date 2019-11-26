#!/usr/bin/env python3

from aws_cdk import core

from auto_cdk.auto_cdk_stack import AutoCdkStack


app = core.App()
AutoCdkStack(app, "auto-cdk")

app.synth()
