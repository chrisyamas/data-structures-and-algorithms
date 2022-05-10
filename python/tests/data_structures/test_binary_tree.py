import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_node_exists():
    assert Node


# @pytest.mark.skip("TODO")
def test_create_node():
    node = Node("apple")
    assert node
    assert node.left is None
    assert node.right is None


# @pytest.mark.skip("TODO")
def test_tree_exists():
    assert BinaryTree


# @pytest.mark.skip("TODO")
def test_tree_root_exists():
    tree = BinaryTree()
    assert tree.root is None


# @pytest.mark.skip("TODO")
def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree


# Happy Path case
def test_find_max_normal_tree():
    tree = BinaryTree()

    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    expected = 7
    actual = tree.find_max()
    assert actual == expected


def test_find_max_all_negative():
    tree = BinaryTree()

    tree.root = Node(-1)
    tree.root.left = Node(-2)
    tree.root.right = Node(-3)
    tree.root.left.left = Node(-4)
    tree.root.left.right = Node(-5)
    tree.root.right.left = Node(-6)
    tree.root.right.right = Node(-7)

    expected = -1
    actual = tree.find_max()
    assert actual == expected

def test_find_max_all_zero():
    tree = BinaryTree()

    tree.root = Node(0)
    tree.root.left = Node(0)
    tree.root.right = Node(0)
    tree.root.left.left = Node(0)
    tree.root.left.right = Node(0)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(0)

    expected = 0
    actual = tree.find_max()
    assert actual == expected


def test_find_max_empty_tree():
    tree = BinaryTree()
    with pytest.raises(IndexError):
        tree.find_max()

