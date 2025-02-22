from setuptools import setup, find_packages

setup(
    name="generic_oauth_nic",
    version="0.1.0",
    description="A generic OAuth authentication library for multiple providers",
    author="Binay Raj Parajuli",
    author_email="binayaparajuli17@egmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
