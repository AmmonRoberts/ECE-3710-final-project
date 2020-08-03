You must have Python 3.8 installed on your computer in order to run this script.

For instructions on how to accomplish this, visit https://www.python.org/.

To install the needed libraries, run "python -m pip install --user numpy scipy matplotlib" from the command line.

To run the script, open a Command Window or terminal in the src folder, then run "python predict.py" or "python3 predict.py", depending on what version of Python your Python path variable points to. 

This Python script automatically imports the raw data from the src/data folder. The CSV files MUST be located in this folder, otherwise the script will not work. The CSV files must also be saved without encoding options, as the script does not support encoding.

The script currently only supports a dataset of 5 items, but this can be changed if n is set equal to the number of tiems in a sample or dataset. 