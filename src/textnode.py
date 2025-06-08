from htmlnode import HTMLNode, LeafNode
from enum import Enum
import re

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
            for item in str:
                if (item.startswith(" ") or item.endswith(" ")):
                    result.append(TextNode(f"{item}", text_type.TEXT))
                else:
                    result.append(TextNode(f"{item}", text_type))
    return result            

def extract_markdown_images(text):
    return  re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)    

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if (extract_markdown_images(node.text) == []):
            result.append(node)
        else:
            str = re.split(r"\!(.*?)\)", node.text)
            if "" in str:
                str.remove("")
            for char in str:
                if char == "":
                    pass
                if (char.startswith(" ") or char.endswith(" ")):
                    result.append(TextNode(f"{char}", TextType.TEXT))
                else:
                    result.append(TextNode("".join(re.findall(r"(?<=\[).*?(?=\])", char)), TextType.IMAGE, "".join(re.findall(r"(?<=\().*", char)) ))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if (extract_markdown_links(node.text) == []):
            result.append(node)
        else:
            str = re.split(r"\[(.*?)\)", node.text)
            if "" in str:
                str.remove("")
            for char in str:
                if char == "":
                    pass
                if (char.startswith(" ") or char.endswith(" ")):
                    result.append(TextNode(f"{char}", TextType.TEXT))
                else:
                    result.append(TextNode("".join(re.findall(r".*?(?=\])", char)), TextType.LINK, "".join(re.findall(r"(?<=\().*", char)) ))
    return result

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result

