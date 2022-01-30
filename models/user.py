#!/usr/bin/python3
"""Module for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    lasr_name = ""