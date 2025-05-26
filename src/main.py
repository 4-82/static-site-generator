from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", "link", "https://boot.dev")
    print(node.__repr__())

main()
