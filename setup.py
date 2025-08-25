#this will to install the package locally
from setuptools import setup, find_packages

setup(
    name = "medical_chatbot",
    version = "0.1.0",
    author="Naman Nirbhaya",
    author_email="namannirbhay9@gmail.com",
    packages=find_packages(),#will find constructor file then it will install as a local poackage
    install_requires=[] # will auto take reuriements from requirements.txt file
)