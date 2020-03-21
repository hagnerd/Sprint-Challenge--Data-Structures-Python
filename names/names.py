import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
def add_all_names_to_bst(list_of_names, search_tree=None, dupes=[]):
    for name in list_of_names:
        if search_tree is None:
            search_tree = BinarySearchTree(name)
        elif not search_tree.contains(name):
            search_tree.insert(name)
        else:
            dupes.append(name)

    return dupes

bst = None
duplicates = add_all_names_to_bst(names_2, bst, add_all_names_to_bst(names_1,
                                                                     bst))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
