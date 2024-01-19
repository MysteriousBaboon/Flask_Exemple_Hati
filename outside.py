from flask import Flask, render_template
import psycopg2
import os
import boto3
from PIL import Image, ImageFilter
import io
import time

boto3.setup_default_session(profile_name='oclock')

s3 = boto3.client('s3')
s3.download_file('bucketanuno', 'drapeau-anne-stokes-pirate-pr.png', 'unaltered.png')

# MODIFY PICTURE
im = Image.open('unaltered.png')
im1 = im.filter(ImageFilter.BLUR)
im1.save('altered.png')
#

s3.upload_file('altered.png', 'bucketanuno', 'drapeau-anne-stokes-pirate-pr-BLURED.png')

log = boto3.client('logs')
response = log.put_log_events(
    logGroupName='mark_betise',
    logStreamName='Test',
    logEvents=[
        {
            'timestamp': round(time.time() * 1000),
            'message': 'Une image a ete lue et modifiee'
        },
    ],
    sequenceToken='string'
)
print(response)

