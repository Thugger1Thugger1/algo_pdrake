class Node:
    def __init__(self, key, left=None, right=None) -> None:
        self.left = left
        self.key = key
        self.right = right
    
    def __str__(self) -> str:
        return f'[{self.left} {self.key} {self.right}]'

    def __repr__(self) -> str:
        return str(self)
    