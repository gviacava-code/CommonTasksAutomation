# File Management
# ---
# Using the `os` and `Pandas` libraries in Python to create folders from an Excel file. 
# The code reads an Excel file with columns A, B, and C and creates corresponding 
# folders structure in the local directory.


import os
import pandas as pd

# read the excel file into a pandas dataframe
df = pd.read_excel('program.xlsx')

# iterate through each row in the dataframe
for index, row in df.iterrows():
    # create the root folder (column A)
    root_folder = row['fieldofStudy']
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)
    
    # create the subfolder (column B)
    subfolder = os.path.join(root_folder, row['courses'])
    if not os.path.exists(subfolder):
        os.mkdir(subfolder)
    
    # create the subfolder of subfolder (column C)
    subfolder_of_subfolder = os.path.join(subfolder, row['topics'])
    if not os.path.exists(subfolder_of_subfolder):
        os.mkdir(subfolder_of_subfolder)
