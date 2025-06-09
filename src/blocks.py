
def markdown_to_blocks(markdown):
    result = list(filter(None, map(lambda x: x.strip(), text.split("\n\n"))))
    return result

