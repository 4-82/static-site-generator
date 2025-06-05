from htmlnode import HTMLNode, LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            (self.text == other.text)
            and (self.text_type == other.text_type)
            and (self.url == other.url)
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type.value:
        case TextType.TEXT.value:
          return LeafNode(None, text_node.text)
        case TextType.BOLD.value:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC.value:
            return LeafNode("i", text_node.text)
        case TextType.CODE.value:
            return LeafNode("code", text_node.text)
        case TextType.LINK.value:
            return LeafNode("a", text_node.text, "href")
        case TextType.IMAGE.value:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError("Type is not in TextType")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if (node.text_type.value != "text"):
            result.append(node)
        else:
            if (node.text.count(delimiter) % 2 != 0):
                raise ValueError("Invalid Markdown Syntax") 
            str = node.text.split(f"{delimiter}")            
            print(str)            
            for item in str:
                if (item.startswith(" ") or item.endswith(" ")):
                    result.append(TextNode(f"{item}", text_type.TEXT))
                else:
                    result.append(TextNode(f"{item}", text_type))
    return result            
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# print(new_nodes)
# print(TextNode("test", TextType.CODE))
