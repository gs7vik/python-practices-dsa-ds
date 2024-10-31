import requests
import json

# Replace with your actual API key
API_KEY = 'f7844e3ddf658beae0535b7fa53b5529b6360c6d'
# The endpoint for the Gemini model
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent'

# Set up headers including your API key for authorization
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Define your request payload
data = {
    "contents": [{
        "role": "user",
        "parts": [{
            "text": "What is the capital of France?"
        }]
    }],
    "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 100
    },
    "systemInstruction": {
        "parts": [{
            "text": "Please respond in a friendly manner."
        }]
    }
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check for successful response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error: {response.status_code}, Message: {response.text}")