import unittest
from htmlnode import HTMLNode, LeafNode

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_to_html_p(self):
    node = LeafNode("a", "https://boot.dev")
    self.assertEqual(node.to_html(), "<a>https://boot.dev</a>")

def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

def test_leaf_properties_exitst(self):
    node = LeafNode("p", "this is a test")
    self.assertIsNotNone(node.tag)
    self.assertIsNotNone(node.value)
