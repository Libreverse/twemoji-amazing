import re
import os

def replace_urls_with_filenames(file_path):
    # Read content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex pattern to match and capture filenames in URLs
    pattern = r'(url\("https://cdn.jsdelivr.net/gh/twitter/twemoji@master/assets/svg/)(.*?)(\.svg"\))'
    
    # Function to use for replacement in re.sub
    def replacement(match):
        return f'url("{match.group(2)}.svg")'

    # Replace URLs with filenames
    new_content = re.sub(pattern, replacement, content)

    # Write back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"File '{file_path}' has been updated.")

# Path to the css file in the current directory
css_file_path = 'twemoji-amazing.css'

if __name__ == "__main__":
    if os.path.exists(css_file_path):
        replace_urls_with_filenames(css_file_path)
    else:
        print(f"Error: The file '{css_file_path}' does not exist in the current directory.")