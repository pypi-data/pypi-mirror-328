from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='please_help_me_solve',
    version='0.2',
    packages=find_packages(),
    install_requires =[
        'google-generativeai>=0.7.2'
    ],
    long_description=description,
    long_description_content_type='text/markdown',
)