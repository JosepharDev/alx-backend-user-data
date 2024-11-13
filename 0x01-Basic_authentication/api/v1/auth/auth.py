#!/usr/bin/env python3
""" define auth module """

from flask import request
from typing import List, TypeVar
from fnmatch import fnmatch


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            check path if exist in excluded_paths
        """
        if path is None:
            return True
        if excluded_paths in None or not excluded_paths:
            return True
        for pt in excluded_paths:
            if fnmatch(path, pt):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            get authorization header from request
        """
        if request is not None:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            get current user from request
        """
        return None
