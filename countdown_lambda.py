import datetime
import boto3

from botocore.exceptions import ClientError

sns = boto3.client('sns')

def lambda_handler(event, context):
    CurrentDate = datetime.datetime.now()
    Leave = "30/01/2020 15:00"
    Leave = datetime.datetime.strptime(Leave, "%d/%m/%Y %H:%M")
    countdown = Leave - CurrentDate
    sns.publish(
                TopicArn='arn:aws:sns:eu-west-1:XXXXXXXXXXXX:countdown',
                Message=("Hello Guilherme! \nYour leave will be in {} days!".format(countdown.days))
            )
