import requests

def info():
    return "AdrianDevProjects Online Services Python SDK Authentication Module v1.1.1_FINAL by Adrian Albrecht"


def login(username, password, return_mode):
    login_url = "https://onlineservices.adriandevprojects.com/v1/auth/login/"

    credentials = {
        "username": username,
        "password": password
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(login_url, data=credentials, headers=headers)

    if return_mode in ("content+code", "code+content"):
        return f"{response.status_code}\n{response.text}"
    elif return_mode == "content":
        return response.text
    elif return_mode == "code":
        return response.status_code
    else:
        return "Invalid return configuration in request"


def register(username, password, return_mode, instant_login=bool):
    register_url = "https://onlineservices.adriandevprojects.com/v1/auth/register/"

    register_credentials = {
        "username": username,
        "password": password,
        "confirm_password": password
    }

    register_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(register_url, data=register_credentials, headers=register_headers)

    if response.status_code == 201:
        if instant_login:
            login(username, password, return_mode)
    else:
        return f"Registration failed: {response.text}"



