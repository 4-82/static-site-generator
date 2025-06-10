from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    result = list(filter(None, map(lambda x: x.strip(), markdown.split("\n\n"))))
    return result


def block_to_block_type(block):
    if (block.startswith("#")):
        return BlockType.HEADING.value
    elif (block[:3] == block[-3:]) and block.startswith("`"):
        return BlockType.CODE.value
    elif (block.startswith(">")):
         if False in list(map(lambda x: x[0] == ">",(block.split("\n")))):
             return False
         return BlockType.QUOTE.value
    elif (block.startswith("-")):
         if False in list(map(lambda x: x[0] == "-" and x[1] == " ", (block.split("\n")))):
             return False
         return BlockType.UNORDERED_LIST.value
    elif (block[:3] == "1. "):
        count = 0
        for str in block.split("\n"):
            if int(str[0]) == (count + 1) and str[1:3] == ". ":
                count += 1
                result = True
            else:
                result = False
        if (result):
            return BlockType.ORDERED_LIST.value            
    return BlockType.PARAGRAPH.value

print(block_to_block_type("1. this is a test\n2. okay \n3. sure"))
