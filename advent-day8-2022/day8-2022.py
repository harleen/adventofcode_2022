
from __future__ import annotations

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.topNode = None
        self.bottomNode = None

    def leftNode(self, node: TreeNode):
        self.leftNode = node

    def rightNode(self, node: TreeNode):
        self.rightNode = node

    def topNode(self, node: TreeNode):
        self.topNode = node

    def bottomNode(self, node: TreeNode):
        self.bottomNode = node

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.value == other.value and self.leftNode == other.leftNode and self.rightNode == other.rightNode and self.topNode == other.topNode and self.bottomNode == other.bottomNode
        return False
    
    def __str__(self):
        return (
            f"{self.value}"
            f"L:{self.leftNode.value if self.leftNode else None}"
            f"R:{self.rightNode.value if self.rightNode else None}"
            f"T:{self.topNode.value if self.topNode else None}" 
            f"B:{self.bottomNode.value if self.bottomNode else None}")


def main():
    parse_file()

def parse_file():

    file_path = 'advent-day8-2022/test_input.txt'#2022-puzzle8-input.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a matrix of Node objects
    matrix = [list(map(TreeNode, map(int, line.strip()))) for line in lines]
    #[list(map(TreeNode, map(int, line.strip()))) for line in lines]
    print(f"{matrix}")

    # Determine the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"{rows},{cols}")

    # Connect neighboring nodes
    for i in range(rows):
        for j in range(cols):
            node = matrix[i][j]

            # Connect top neighbor
            node.topNode = matrix[i - 1][j] if i - 1 >= 0 else None

            # Connect bottom neighbor
            node.bottomNode = matrix[i + 1][j] if i + 1 < rows else None

            # Connect left neighbor
            node.leftNode = matrix[i][j - 1] if j - 1 >= 0 else None

            # Connect right neighbor
            node.rightNode = matrix[i][j + 1] if j + 1 < cols else None

            print(f"{node}")

    return matrix


if __name__ == "__main__":
    main()