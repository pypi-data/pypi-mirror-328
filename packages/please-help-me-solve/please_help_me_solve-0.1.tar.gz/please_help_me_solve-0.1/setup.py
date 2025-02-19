from setuptools import setup, find_packages

setup(
    name='please_help_me_solve',
    version='0.1',
    packages=find_packages(),
    install_requires =[
        'google-generativeai>=0.7.2'
    ]
)