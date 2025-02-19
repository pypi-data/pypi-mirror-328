from importlib import resources
from shutil import copyfile
import os

import pandas as pd


def load(file):
    # Ensure file has .zip extension
    file += '.zip' * (not file.endswith('.zip'))

    # Absolute path to data
    abs_path = resources.files("jrpyintroduction") / "data" / file

    return pd.read_csv(abs_path)


def populate_examples():
    # Get absolute path to data folder
    data_path = resources.files("jrpyintroduction") / "data"

    # Get list of data files
    pkg_data = os.listdir(data_path)

    # Drop compressed files
    files = [file for file in pkg_data if not file.endswith('.zip')]

    # Copy files to current dir
    for file in files:
        abs_path = data_path / file
        copyfile(abs_path, file)
        print(f'\nCreated file {file} in current directory.\n')
