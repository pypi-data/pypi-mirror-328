from setuptools import setup, find_packages

setup(
    name="user-management",
    version="0.5.3",
    packages=find_packages(),
    install_requires=[
        "firebase-admin>=6.4.0",
        "pydantic>=2.0.0",
        "python-jose[cryptography]>=3.3.0",
        "boto3>=1.34.0",
        "stripe>=7.10.0"
    ],
    author="Brennen",
    author_email="brennen.barney@gmail.com",
    description="A user management package using Firebase",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clickstack/user-management",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 