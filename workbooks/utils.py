# import the data handling library
from optparse import Option
import os
from tkinter import E
from turtle import st
from urllib import request
import pandas as pd
from pandas import DataFrame
from typing import List, Optional
import urllib

# define a prefix
PREFIX = "https://github.com/phuse-org/phuse-scripts/raw/master/data/sdtm/cdiscpilot01/"

def check_link(url: str) -> bool:
    """
    ensure that the URL exists
    """
    # this will attempt to open the URL, and extract the response status code
    # - status codes are a HTTP convention for responding to requests
    # 200 - OK
    # 403 - Not authorized   
    # 404 - Not found   
    status_code = urllib.request.urlopen(url).getcode()
    return status_code == 200


def load_cdiscpilot_dataset(domain_prefix: str) -> Optional[DataFrame]:
    """
    load a CDISC Pilot Dataset from the GitHub site
    @param domain_prefix: the Domain Prefix for the Domain (eg DM, VS)
    """
    # define the target for our read_sas directive
    target = f"{PREFIX}{domain_prefix.lower()}.xpt"
    # make sure that the URL exists first
    if check_link(target):
        # let pandas work it out
        dataset = pd.read_sas(target, encoding="utf-8")
        return dataset
    return None


def convert_cdiscpilot_dataset(domain_prefix: str, output_dir: str) -> Optional[DataFrame]:
    """
    load a CDISC Pilot Dataset from the GitHub site and write it out to a CSV file
    @param domain_prefix: the Domain Prefix for the Domain (eg DM, VS)
    @param output_dir: the directory into which we want to write the content
    """
    dataset = load_cdiscpilot_dataset(domain_prefix)
    if dataset:
        if os.path.exists(output_dir):
            target_file = os.path.join(output_dir, f"{domain_prefix.lower()}.csv")
            dataset.to_csv(target_file, index=False, header=True)
        else:
            print(f"{output_dir} does not exist")
    else:
        print(f"Unable to load dataset for {domain_prefix}")

