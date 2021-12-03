import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('minorProject')

def lambda_handler(event, context):
    print (event)
    name = event['name']
    mobile = event['mobile']
    email = event['email']
    table.put_item(
            Item={
                'name': name,
                'mobile':mobile,
                'email':email,
            }
        )
    return 'added record successfully'