from setuptools import setup, find_packages

setup(
    name='singtown_ai_mock_server',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
    ],
    package_data={
        'singtown_ai_mock_server': ['media/**/*', '*.json'],
    },
)