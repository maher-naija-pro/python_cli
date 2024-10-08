#!/usr/bin/python
from typing import Optional
import typer
import time
import json
from rich import print

from neurodeploy import model

model_app = typer.Typer()


@model_app.command("push")
def model_push(
    name: str = typer.Option(..., help="Your model name"),
    filepath: str = typer.Option("None", help="Your model file path on your computer"),
    lib: str = typer.Option("tensorflow", help="Your model library"),
    filetype: str = typer.Option("h5", help="Your model persistance type"),
):
    """
    #model create update
    """
    resp = model.push(name, filepath, lib, filetype)
    print(resp)


@model_app.command("delete")
def model_delete(name: str = typer.Option(..., help="Your model name to delete")):
    """
    #model delete
    """
    resp = model.delete(name)
    print(resp)


@model_app.command("get")
def model_get(name: str = typer.Option(..., help="Your model name to get info")):
    """
    #model get
    """
    resp = model.get(name)
    print(resp)


@model_app.command("list")
def models_list():
    """
    #model get
    """
    resp = model.list()
    print(resp)


@model_app.command("predict")
def model_predict(
    name: str = typer.Option(..., help="Your model name"),
    data: str = typer.Option(..., help="Your payload"),
):
    """
    #model predict
    """
    resp = model.predict(name, json.loads(data))
    print(resp)
