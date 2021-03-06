import time
# using Binary Search Tree data strcuture to hold names names
# only insert & contains are needed
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    # Insert the given value into the tree
    def insert(self, value):
        #check if new value is less than current node
        if value < self.value:
            # there is NO self.left value
            if not self.left:
                # set NEW left child as as new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)    
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True
        sub_tree_contains = False
        if target < self.value:
            if not self.left:
                return False
            else:
                #return self.left.contains(target)
                sub_tree_contains = self.left.contains(target)        
        # target is larger, go right
        else: 
            if not self.right:
                return False
            else:
                sub_tree_contains = self.right.contains(target)    
        return sub_tree_contains
start_time = time.time()
f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# Double for loops cause a nasty COMPLEXITY of O(n^2),  run takes about 6 secs 
# duplicates = []
duplicates = []
# set 
bst = BinarySearchTree(names_1[0])
#! add in names    - takes about .110 sec
for i in range(1, len(names_1)):
    bst.insert(names_1[i])
# verify contains works
#! do compare from names_2     - NOW takes about .12 - .14 seconds
for i in range(len(names_2)):
    if bst.contains(names_2[i]):
        duplicates.append(names_2[i])
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")