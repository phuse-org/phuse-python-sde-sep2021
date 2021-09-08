# PHUSE SDE 2021 Python Session

This is the material for the PHUSE SDE Event regarding the use of Python

## Setup
We recommend that you use Visual Studio Code as a client for the Workbooks
* Install the Python Extension

## Installing
1. Clone the project using git
    `git clone https://github.com/phuse-org/phuse-python-sde-sep2021`
2. Install Python
    * Windows - https://www.python.org/downloads/windows/ -> Windows Installer (64bit)
    * OSX - Install using homebrew (https://brew.sh/) -> `brew install python`
    * Linux - Follow your packaging environment guide (eg apt)
3. Install Pipenv (a python environment management tool)
    * `pip install --user pipenv`
4. Install the dependencies
    * `pipenv install`
5. Create a file called `.env` and in it put the following (replace `<token>` with your CDISC Library Token)
    `CDISC_LIBRARY_API_TOKEN=<token>`
6. Open the folder using Visual Studio Code


