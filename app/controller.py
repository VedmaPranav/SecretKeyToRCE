from datetime import datetime
import requests
import subprocess


def get_data():
    response = requests.get("https://dummyjson.com/products/1")
    return response.json()


def get_token():
    guest_user = "guest@key.user" + "|" + str(datetime.now().timestamp()) + "|" + "KeyInc"
    print(guest_user)
    encrypted_user = subprocess.check_output("java -jar Encryptor.jar "+guest_user, shell=True, text=True)
    encrypted_token = encrypted_user.split(":")[1].strip()
    return encrypted_token


print(get_token())
