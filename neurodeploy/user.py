from rich import print

from utils import query
from process import nd_credentials
from process import nd_token
from process import nd_config


def login(username: str, password: str) -> str:
    """login user to get jwt token saved on conf file.

    :params: username
    :type:   str
    :params: password
    :type:   str
    :returns: ok.
    :rtype: dict
    :raises: none

    >>> from neurodeploy import users
    >>> users.login(username, password)
    """
    conf = nd_config.save_config(username)
    conf = nd_config.read_saved_config()
    if "url" not in conf:
        return {
            "status_code": 400,
            "message": "Could not read config file. Plase run configure first.",
        }
    if "status_code" in conf:
        print("[bold red]cant login run config before[/bold red]")
        return {"message": "cant login run config before", "status_code": 400}

    main_url = conf["url"]
    url = main_url + "/sign-in"
    headers = {"username": username, "password": password}

    data = None
    response_data = query.post(url, data, headers)
    if response_data.get("status_code", 400) != 200:
        print("[bold red]login error[/bold red]")
        return {"message": "login error", "status_code": 400}
    else:
        print("[green]Login Successful[/green]")
        resp = nd_token.save_token(response_data)
        if "status_code" in resp:
            if resp["status_code"] == 200:
                print("[bold green]Your token is saved[/bold green]")
                return {"message": "Your token is saved", "status_code": 200}
            else:
                print("[bold red]Cant save your token[/bold red]")
                return {"message": "Cant save your token", "status_code": 400}
    return {"message": "Login Successful", "status_code": 200}
