
### Overview

This repository contains Python code to combine multiple files into a single DataFrame and split a DataFrame into smaller files based on row intervals. The main purpose is to streamline the handling of data stored in multiple files and provide a convenient method for processing large datasets.

### Import Libraries

The code relies on the following libraries:

-   **os**: Provides functions for interacting with the operating system, essential for file manipulation.
-   **pandas (pd)**: Offers data structures and operations for manipulating numerical tables and time series. It is extensively used for data analysis and manipulation.

### Functions

#### 1. `combine_files(folder_path, file_type='xlsx')`

-   **Description**: Combines all XLSX or CSV files within a specified folder into a single DataFrame.
-   **Parameters**:
    -   `folder_path` (str): Path to the folder containing the files.
    -   `file_type` (str): Type of files to combine, either 'xlsx' or 'csv'. Default is 'xlsx'.
-   **Returns**:
    -   `DataFrame`: Combined DataFrame.

#### 2. `split_and_save_dataframe(df, interval, file_type='csv')`

-   **Description**: Splits a DataFrame into user-defined row intervals and saves them into separate files.
-   **Parameters**:
    -   `df` (pandas.DataFrame): The DataFrame to be split.
    -   `interval` (int): The number of rows per interval.
    -   `file_type` (str): The type of file to save ('csv' or 'xlsx'). Default is 'csv'.
-   **Returns**:
    -   None

### Usage

1.  **Combine Files**:
    
    -   Call the `combine_files` function with the folder path where the files are located and the desired file type.
    -   Example:
        
        pythonCopy code
        
        `Folder_path = "/workspaces/ConcatNSplit/Data Folder"
        combined_df = combine_files(Folder_path , 'csv')
        print(combined_df)` 
        
2.  **Split DataFrame into Small Files**:
    
    -   Call the `split_and_save_dataframe` function with the DataFrame, desired row interval, and file type.
    -   Example:
        
        pythonCopy code
        
        `split_and_save_dataframe(combined_df , 2 , 'xlsx')` 
        
        This will split the combined DataFrame into intervals of 2 rows each and save them as XLSX files.

### Note

-   Ensure that the folder path provided for file operations is accurate and accessible.
-   Adjust the row interval according to your specific requirements.
-   Supported file types for splitting are 'csv' and 'xlsx'.

### Author

-   This code was authored by an individual with expertise in Python programming and data manipulation.

### License

-   This code is provided under the MIT License.
