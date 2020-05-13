"""
This module provides a help class to dynamically loads and present classes and
modules for both swagger docs and the zenwebserver.
"""
from importlib import import_module
from inspect import ismethod


class Loader:
    """
    A convenience class for dynamically loading webserver modules.
    """
    @staticmethod
    def get_class(module, class_name):
        """ Return the class definition given the name of the module and class.
        """
        mod = import_module(module)
        return getattr(mod, class_name)

    @staticmethod
    def get_public_methods(obj):
        """ Return a list of the public methods of the given object. """
        return [method_name for method_name in dir(obj)
                if ismethod(getattr(obj, method_name))
                and method_name[0] != "_"]
