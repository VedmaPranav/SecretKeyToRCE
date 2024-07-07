from datetime import datetime
import requests
import subprocess


def get_data():
    response = requests.get("https://dummyjson.com/products/1")
    return response.json()


def get_user_token():
    guest_user = "guest@key.user" + "_" + str(datetime.now().timestamp()) + "_" + "KeyInc"
    encrypted_user = encrypt_user(guest_user)
    encrypted_token = encrypted_user.split(":")[1].strip()
    return encrypted_token


def encrypt_user(user: str):
    return subprocess.check_output("java -jar Encryption/Encryptor.jar " + user + " 1", shell=True, text=True)


def decrypt_token(token: str):
    return subprocess.check_output("java -jar Encryption/Encryptor.jar " + token + " 0", shell=True, text=True)



print(get_user_token())

