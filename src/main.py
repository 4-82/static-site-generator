import os, shutil
from blocks import markdown_to_html_node

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

def extract_markdown_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

    from_file = open(from_path)
    from_file_text = from_file.read()
    from_file.close()

    template = open(template_path)
    template_file_text = template.read()
    template.close()

    file = markdown_to_html_node(from_file_text)
    file = file.to_html()
    title = extract_markdown_title(from_file_text)
    template = template_file_text.replace("{{ Title }}", title)
    template = template_file_text.replace("{{ Content }}", file)
    if not (os.path.exists(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    if os.path.exists(os.path.join(dest_path, "index.html")):
        pass
    else:
        with open(os.path.join(dest_path, "index.html"), "w") as page:
            page.write(template_file_text)
        page.close()
