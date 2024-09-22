#!/usr/bin/python
import typer
import sys
from rich import print


import neurodeploy

import sub_cmd.user as user
import sub_cmd.model as model
import sub_cmd.credentials as credentials

# import sub_cmd.config as config
import process.nd_config as config
import process.nd_credentials as nd_credentials


##########################################################
app = typer.Typer()
app.add_typer(model.model_app, name="model", help="Manage models")
app.add_typer(
    credentials.credentials_app, name="credentials", help="Manage user credentials"
)
# app.add_typer(user.user_app, name="user", help="Manage user auth")
# app.add_typer(config.config_app, name="config", help="Manage user config")
#############################################################


@app.command("login")
def user_login(username: str = typer.Option(...), password: str = typer.Option(...)):
    """
    #user create
    """
    neurodeploy.user.login(username, password)


@app.command()
def configure(
    username: str = typer.Option(
        ..., prompt="Enter your username", help="user username created with ui"
    ),
    password: str = typer.Option(
        ...,
        prompt="Enter your password",
        help="user password created with ui",
        confirmation_prompt=True,
        hide_input=False,
    ),
    credential_name: str = typer.Option(
        ..., prompt="Enter your credential name", help="user credential name"
    ),
):
    conf = config.save_config(username)
    print(conf["message"])
    log = neurodeploy.user.login(username, password)
    if log.get("status_code", 400) == 200:
        cred = neurodeploy.credentials.create(
            credential_name, "credential_of_" + username
        )
        if "error_message" in cred:
            print(
                f'{cred["error_message"]} Please note that your credentials has not been updated locally.'
            )
        else:
            print(cred.get("error_message", "credential created"))

        if cred.get("status_code", 200) == 200:
            save_cred = nd_credentials.save_credentials(cred)
            print(save_cred.get("message"))


@app.command("deploy")
def model_push(
    name: str = typer.Option(..., help="Your model name"),
    filepath: str = typer.Option("None", help="Your model file path on your computer"),
    lib: str = typer.Option("tensorflow", help="Your model library"),
    filetype: str = typer.Option("h5", help="Your model persistance type"),
):
    """
    #model create update
    """
    resp = neurodeploy.model.push(name, filepath, lib, filetype)
    print(resp)


if __name__ == "__main__":
    app()
