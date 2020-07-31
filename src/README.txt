You must have a recent version of Python installed on your computer in order to run this script.

For instructions on how to accomplish this, visit https://www.python.org/.

To install the needed libraries, run "python -m pip install --user numpy scipy matplotlib" from the command line.

This Python script automatically imports the raw data from the src/data folder. The CSV files MUST be located in this folder, otherwise the script will not work. The CSV files must also be saved without encoding options, as the script does not support encoding.

The script currently only supports a dataset of 5 items, but this can be changed if n is set equal to the number of tiems in a sample or dataset. 