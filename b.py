import os
from opencc import OpenCC

def convert_filename_to_simplified(directory):
    """
    Convert all markdown file names in the given directory from traditional to simplified Chinese.
    """
    # Initialize the OpenCC converter to convert from Traditional to Simplified Chinese
    cc = OpenCC('t2s')
    
    # Iterate over all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is a markdown file
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Convert the filename to simplified Chinese
                simplified_filename = cc.convert(file)
                simplified_file_path = os.path.join(root, simplified_filename)
                
                # Rename the file
                os.rename(file_path, simplified_file_path)

# Execute the function on the current directory
convert_filename_to_simplified('.')