################ import libraries ################
import os
import pandas as pd

################ Combine files function ################
def combine_files(folder_path, file_type='xlsx'):
    """
    Combine all XLSX or CSV files in a given folder path.

    Parameters:
        folder_path (str): Path to the folder containing files.
        file_type (str): Type of files to combine, either 'xlsx' or 'csv'. Default is 'xlsx'.

    Returns:
        DataFrame: Combined DataFrame.
    """
    # Convert file_type to lowercase for case-insensitive comparison
    file_type = file_type.lower()
    
    # List to store DataFrames of each file
    df_list = []

    # Loop through files in the folder
    for file in os.listdir(folder_path):
        # Check if the file ends with the specified file type
        if file.endswith('.' + file_type):
            # Construct the full file path
            file_path = os.path.join(folder_path, file)
            # Read the file based on its type and append to the list
            if file_type == 'xlsx':
                df_list.append(pd.read_excel(file_path))
            elif file_type == 'csv':
                df_list.append(pd.read_csv(file_path))

    # Check if any files were found
    if not df_list:
        raise FileNotFoundError(f"No {file_type.upper()} files found in the folder.")

    # Combine all DataFrames in the list
    combined_df = pd.concat(df_list, ignore_index=True)

    return combined_df

################ File path ################
Folder_path = "/workspaces/ConcatNSplit/Data Folder"
df = combine_files(Folder_path , 'csv')
print(df)
