---
author: Vasken Dermardiros
categories: note
tags:
- reference
title: Data Types
links:
- https://www.bigocheatsheet.com/
- https://realpython.com/python-data-structures/
---

Also see [[big_O]] for complexities associated to the data types.

# Common data types
+ Array : `[1,2,3]` which is a list or a tuple
+ Stack: A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. Can still use a python list but only with `[].pop()`
+ Heap: a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of the heap (with no parents) is called the root node.
  + Priority queue
+ Queue: store items in a First-In/First-Out (FIFO) manner.
  + Sometimes there's a peek command for these 2 ^ where you can view the next item without popping it out.
+ Singly-linked list: a linked list that contains data and a reference to the next node.
  + ![Diagram of inserting a node into a singly linked list](../attachments/2022-12-07-15-01-45.png)
+ Doubly-linked list: same as above but each node has a reference also to the previous one
  + ![A doubly linked list whose nodes contain three fields: the link to the previous node, an integer value, and the link to the next node.](../attachments/2022-12-07-15-03-07.png)
+ Skip list: linked list structure with multiple levels to help with search. Best to check the [wiki page](https://en.wikipedia.org/wiki/Skip_list).
  + ![A schematic picture of the skip list data structure. Each box with an arrow represents a pointer and a row is a linked list giving a sparse subsequence; the numbered boxes (in yellow) at the bottom represent the ordered data sequence. Searching proceeds downwards from the sparsest subsequence at the top until consecutive elements bracketing the search element are found.](../attachments/2022-12-07-15-05-26.png)
  + The elements used for a skip list can contain more than one pointer since they can participate in more than one list.
  + Requires more space to store
+ Hash table: In computing, a hash table, also known as hash map, is a data structure that implements an associative array or dictionary. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.
  + ![A small phone book as a hash table](../attachments/2022-12-07-15-09-16.png)
+ Binary search tree (BST): sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree.
  + ![A binary search tree of size 9 and depth 3, with 8 at the root. The leaves are not drawn.](../attachments/2022-12-07-15-12-45.png)
  + See the [wiki page](https://en.wikipedia.org/wiki/Binary_search_tree) on how to add/delete elements from the tree
  + A BST can be traversed through 3 basic algorithms:
    + Inorder tree walk: Nodes from the left subtree get visited first,     followed by the root node and right subtree.
    + Preorder tree walk: The root node gets visited first, followed by left  and right subtrees.
    + Postorder tree walk: Nodes from the left subtree get visited first, followed by the right subtree, and finally the root.
+ Cartesian tree: binary tree derived from a sequence of numbers; it can be uniquely defined from the properties that it is heap-ordered and that a symmetric (in-order) traversal of the tree returns the original sequence.
  + ![Numbers to Cartesian tree](../attachments/2022-12-07-15-18-04.png)
+ B-tree is a self-balancing tree that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. The B-tree generalizes the binary search tree, allowing for nodes with more than two children.
+ Red-black tree: a kind of self-balancing binary search tree. Each node stores an extra bit representing "color" ("red" or "black"), used to ensure that the tree remains balanced during insertions and deletions.
  + https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
+ Splay tree: is a binary search tree with the additional property that recently accessed elements are quick to access again.
+ AVL tree: (named after inventors Adelson-Velsky and Landis) is a self-balancing binary search tree. It was the first such data structure to be invented. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.
+ k-d tree (short for k-dimensional tree) is a space-partitioning data structure for organizing points in a k-dimensional space. k-d trees are a useful data structure for several applications, such as searches involving a multidimensional search key (e.g. range searches and nearest neighbor searches) and creating point clouds. k-d trees are a special case of binary space partitioning trees.


## Queue
+ https://docs.python.org/3/library/queue.html

``` python
import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')
```

[//begin]: # "Autogenerated link references for markdown compatibility"
[big_O]: big_O.md "Big O notation"
[//end]: # "Autogenerated link references"
