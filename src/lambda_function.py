import os
import json
import requests

NEXT_PUBLIC_PORTFOLIO_API_URL = os.environ['NEXT_PUBLIC_PORTFOLIO_API_URL']
PORTFOLIO_PRIVATE_API_KEY = os.environ['PORTFOLIO_PRIVATE_API_KEY']
USER_EMAIL = os.environ['USER_EMAIL']

api_key = f"Bearer ${PORTFOLIO_PRIVATE_API_KEY}"

headers = {
    "Authorization": api_key,
    "User-Email": USER_EMAIL
}

def lambda_handler(event, context):
    return requests.get(NEXT_PUBLIC_PORTFOLIO_API_URL, headers=headers)