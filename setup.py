# coding: utf-8

"""
    Cobo Wallet as a Service 2.0

    Contact: help@cobo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "cobo-waas2"
VERSION = "1.13.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
    "PyNaCl==1.5.0",
    "ecdsa==0.19.0",
    "fastapi==0.103.2",
    "uvicorn==0.22.0",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Cobo Wallet as a Service 2.0",
    author="Cobo WaaS",
    author_email="help@cobo.com",
    url="https://github.com/CoboGlobal/cobo-waas2-python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "Cobo Wallet as a Service 2.0"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description_content_type='text/markdown',
    long_description=long_description,
    package_data={"cobo_waas2": ["py.typed"]},
)
