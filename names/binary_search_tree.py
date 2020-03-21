""" MODULE DOC STRING """

class BinarySearchTree:
    """ CLASS DOC STRING """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """ Insert the given value into the tree """
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
            return

        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)

    def contains(self, target):
        """
        Return True if the tree contains the value
        False if it does not
        """
        if target == self.value:
            return True

        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)

        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)

    def get_max(self):
        """ Return the maximum value found in the tree """
        return self.value if self.right is None else self.right.get_max()

    def for_each(self, cb):
        """
        Call the function `cb` on the value of each node
        You may use a recursive or iterative approach
        """

        if self.left is not None:
            self.left.for_each(cb)

        cb(self.value)

        if self.right is not None:
            self.right.for_each(cb)
