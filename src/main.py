import os, shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    handle_file_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        (dir_path_public),
    )

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
