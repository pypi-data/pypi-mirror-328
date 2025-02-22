
import requests
import os
from .logger import logger

url = f"https://api.laserfocus.space"

def access_api(endpoint, method='GET', data=None):
    try:
        # Add timeout to prevent hanging
        auth = requests.post(url + '/login', json={'token': 'laserfocused'})

        if auth.json()['status'] != 'success':
            raise Exception(auth.json()['content'])
        
        response = requests.request(method, url + endpoint, json=data, headers={
            'Authorization': f'Bearer {auth.json()["content"]}'
        })
        
        try:
            return response.json()
        except:
            return response.content
            
    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {str(e)}")
        raise