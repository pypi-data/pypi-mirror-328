from setuptools import setup, find_packages

setup(
    name="azrmail",
    version="0.1.1",
    author="chard",
    author_email="chard@azr.tools",
    description="A Python wrapper for AZRMail API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chardWTF/azrmail.py",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
