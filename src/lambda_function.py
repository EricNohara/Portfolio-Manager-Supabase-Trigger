import os
import requests

NEXT_PUBLIC_PORTFOLIO_API_URL = os.environ['NEXT_PUBLIC_PORTFOLIO_API_URL']
PORTFOLIO_PRIVATE_API_KEY = os.environ['PORTFOLIO_PRIVATE_API_KEY']
USER_EMAIL = os.environ['USER_EMAIL']

headers = {
    "Authorization": f"Bearer {PORTFOLIO_PRIVATE_API_KEY}",
    "User-Email": USER_EMAIL
}

def lambda_handler(event, context):
    response = requests.get(NEXT_PUBLIC_PORTFOLIO_API_URL, headers=headers)
    return {
        "statusCode": response.status_code,
        "body": response.text
    }