import os
from opencc import OpenCC

def convert_markdown_to_simplified(directory):
    """
    Convert all markdown files in the given directory from traditional to simplified Chinese.
    """
    # Initialize the OpenCC converter to convert from Traditional to Simplified Chinese
    cc = OpenCC('t2s')
    
    # Iterate over all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is a markdown file
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Convert the content to simplified Chinese
                simplified_content = cc.convert(content)
                
                # Write the converted content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(simplified_content)

# Execute the function on the current directory
convert_markdown_to_simplified('.')