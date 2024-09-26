import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

def get_employees(event, context):
    response = table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }

def add_employee(event, context):
    body = json.loads(event['body'])
    table.put_item(Item=body)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'SUCCESS'})
    }
