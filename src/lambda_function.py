import json

def lambda_function(event, context):
    return  {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda and GitHub actions!')
    }