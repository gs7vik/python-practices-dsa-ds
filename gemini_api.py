import os
import requests

gemini_key = 'AIzaSyDmc-buN5VJotwI2MR732DM_cZQEhHIlmo'  # Replace 'asd' with your actual API key
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent'
headers = {
    "Content-Type": "application/json"
}
payload = {
    "contents": [
       
       {"parts":[{"text":"you are an expert at answering quesition by appending 2203 at beginning of every response."},{"text":"what is your name"}]}
    ]
}


# Send the request with the API key as a URL parameter
response = requests.post(url, headers=headers, json=payload, params={'key': gemini_key})
response_data = response.json()
print(response_data)
