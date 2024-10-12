#*args demonstration
def multiply(*numbers):
    result=1
    for num in numbers:
        result=result*num
    return result

print(multiply(1,2,3))
print(multiply(20))
print(multiply(3,4))

def log_message(level, *args):
    formatted_message = ' '.join(map(str, args))
    print(f"[{level}] {formatted_message}")

log_message("INFO", "User", "logged", "in")
log_message("ERROR", "File", "not", "found")

#kwargs demonstration 
def process_preferences(**preferences):
    for key, value in preferences.items():
        print(f"{key}: {value}")

process_preferences(username="alice", age=30, city="Wonderland")

def build_api_request(url, **params):
    full_url = url + '?' + '&'.join(f"{key}={value}" for key, value in params.items())
    return full_url

api_url = "https://api.example.com/data"
params = {'page': 1, 'limit': 10, 'sort': 'desc'}
full_request_url = build_api_request(api_url, **params)
print(full_request_url)
