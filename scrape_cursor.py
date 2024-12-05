import requests
from bs4 import BeautifulSoup
import re
import os

print("Script started...")

# Set the base URL
base_url = 'https://cursor.directory'
print(f"Connecting to {base_url}")

# Create a session
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (compatible; WebScraper/1.0)'})

# Fetch the main page
response = session.get(base_url)
print(f"Response status code: {response.status_code}")
print(f"Response content length: {len(response.content)}")

# Parse the main page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <code> elements with the class "text-sm block pr-3"
code_blocks = soup.find_all('code', class_='text-sm block pr-3')
print(f"Found {len(code_blocks)} code blocks")

# Create an output directory for the text files
output_dir = "cursor_directory_code"
os.makedirs(output_dir, exist_ok=True)

# Write each <code> block's content to a separate file
for idx, code_block in enumerate(code_blocks, start=1):
    # Get the text content
    code_content = code_block.get_text(strip=True)
    
    # Generate a filename
    filename = f"rule_{idx}.txt"
    filepath = os.path.join(output_dir, filename)
    
    # Save the content to a file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(code_content)
    
    print(f"Saved: {filepath}")

print(f"Completed! {len(code_blocks)} files written to '{output_dir}' directory.")