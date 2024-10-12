import requests
from datetime import datetime
import logging

logging.basicConfig(filename='clockinout.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def job():

    ip = requests.get('https://api.ipify.org').text
    print(f'My public IP address is: {ip}')

    base_url = "https://api.sumhr.io:3000/api"
    endpoint = f"/attendance/initwebpunch/{ip}"
    url = base_url + endpoint
    bearer_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjQ3NjAyLCJhY2NvdW50aWQiOjcyMCwic3Vic2NyaXB0aW9uaWQiOjc2MSwiZW1wbG95ZWVpZCI6NzMxMzYsInRpbWV6b25laWQiOjI1MSwicm9sZWlkIjoyMzMwLCJtYXN0ZXJwcm9maWxlaWQiOjcsImxvZ2luaW5mb2lkIjo0NDI2NDE0LCJlbWFpbGlkIjoic2F0dmlrLmdzQHRob3VnaHRjbGFuLmNvbSIsImV4cCI6MTcyODAxNjE0OSwiaWF0IjoxNzI3NDExMzQ5fQ.j7wDHDOk0whEaRwzGgtQZ-FWhEmgZkS1gWcqK2GR958"
    



    
    headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }

       
    response = requests.get(url, headers=headers)

        
    if response.status_code == 200:
        logging.info("Request successful!")
        logging.info("Response content: %s", response.json())
    else:
        logging.error("Request failed with status code: %d", response.status_code)
        logging.error("Response content: %s", response.text)
        


if __name__ == "__main__":
    job()
