#!/usr/bin/python3


class User:


    def __init__(self,*args, **kwargs):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_on = created_on

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(user_id, username)

    @property
    def fullName(self):
        return '{} {}'.format(user_id, username)

    @property
    def created_on(self):
        pass

