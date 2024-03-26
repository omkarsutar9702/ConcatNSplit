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

################ Split Data Frame into small files ################
def split_and_save_dataframe(df, interval, file_type='csv'):
    """
    Split a DataFrame into user-defined row intervals and save them into files with sequential names.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be split.
        interval (int): The number of rows per interval.
        file_type (str): The type of file to save ('csv' or 'xlsx'). Default is 'csv'.

    Returns:
        None
    """
    # Calculate total number of rows in the DataFrame
    total_rows = len(df)
    # Calculate total number of intervals needed
    num_intervals = total_rows // interval + (1 if total_rows % interval != 0 else 0)
    
    # Iterate over each interval
    for i in range(num_intervals):
        # Calculate start and end index for the current interval
        start_idx = i * interval
        end_idx = min((i + 1) * interval, total_rows)
        # Slice the DataFrame to get the current interval
        interval_df = df.iloc[start_idx:end_idx]
        
        # Generate file name for the current interval
        file_name = f"output_{i+1}.{file_type}"
        
        # Save interval DataFrame to file based on file_type
        if file_type == 'csv':
            interval_df.to_csv(file_name, index=False)
        elif file_type == 'xlsx':
            interval_df.to_excel(file_name, index=False)
        else:
            # Raise ValueError if file_type is not supported
            raise ValueError("Unsupported file type. Please choose either 'csv' or 'xlsx'.")


################ Folder path to save files ################

split_and_save_dataframe(df , 2 , 'xlsx')