from setuptools import setup

setup(
    name="trimetpy",
    version="0.2.1",
    py_modules=["trimetpy"],
    install_requires=[
        "requests"
    ],
    description="Python library for the TriMet API with OOP, currently lets you fetch all running vehicles, and track individual vehicle IDs. Now includes Portland Streetcar vehicles as well."
)