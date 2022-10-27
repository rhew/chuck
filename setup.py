""" chucks package """
from distutils.core import setup

setup(
    name="chuck",
    version="1.0",
    license="Chuck all rights reserved",
    long_description=open("README.md").read(),
    install_requires=["requests"],
    entry_points={"console_scripts": ["chuck = chuck:main"]},
)
