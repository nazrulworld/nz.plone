# _*_ coding: utf-8 _*_

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup


setup(
    name='nz.plone',
    version='1.dev0',
    url='http://pypi.python.org/pypi/nz.plone',
    description="Plone Management Utility by Nazrul",
    author="Md. Nazrul Islam",
    author_email="connect2nazrul@gmail.com",
    long_description=None,
    packages=["nz", "nz.plone", "nz.plone.install"],
    package_dir={"": "src"},
    namespace_packages=["nz"],
    include_package_data=True,
    install_requires=["setuptools", "six"],
    zip_safe=False,
    entry_point={
        "console_scripts": {
            "plone": ["nz.plone.cli:main"]
        }
    }
)

