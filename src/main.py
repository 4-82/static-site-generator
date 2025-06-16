import os, shutil
from textnode import TextNode, TextType

def main():
    pass

def handle_file_recursive(source="./static", destination="/home/alice/projects/bootdev/static-site-generator/public"):
    if not (os.path.exists(destination)):
        os.mkdir(destination)
    for content in (os.listdir(source)):
        filepath = os.path.join(source, content)
        if (os.path.isfile(filepath)):
            shutil.copy2(filepath, destination)
        else:
            handle_file_recursive(os.path.join(source, content), os.path.join(destination, content))
    
handle_file_recursive()
