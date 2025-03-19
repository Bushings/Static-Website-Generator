from textnode import TextNode, TextType

def main():
    test = TextNode("Anchor text", "link", "www.boot.dev")
    print(test.__repr__())

main()