#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'username': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'password': 'str',
            'phone': 'str',
            'user_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'password': 'password',
            'phone': 'phone',
            'user_status': 'userStatus'
        }

        self._id = None
        self._username = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._password = None
        self._phone = None
        self._user_status = None    # User Status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, user_status):
        self._user_status = user_status

    def __repr__(self):
        properties = []
        for p in self.__dict__:
            if p != 'swaggerTypes' and p != 'attributeMap':
                properties.append('{prop}={val!r}'
                                  .format(prop=p, val=self.__dict__[p]))

        return '<{name} {props}>'.format(name=__name__,
                                         props=' '.join(properties))
