# _*_ coding: utf-8 _*_
__author__ = 'nislam <connect2nazrul@gmail.com>'
# Zope Style
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)

except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)
