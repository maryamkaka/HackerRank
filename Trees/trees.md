## Trees

### Binary Trees
```` Text
      A       <- Root
     / \
    B   C     <- Child
   / \   \
  D  E    G   <- Leaf
````
- only two children (left and right)
- children can be null
- __Balanced Tree__: roughly the same number of node are on the left and right side of the tree

#### Binary Search Trees
- on any subtree the left node is less than the root node which is less than any of the right nodes
- decreases search time (each iteration will cut the tree down by half)
- ##### Insersion
  - new value is compared to root value
    - if less than root go left else go right
    - continue until you reach null node then insert
  - order of values matter (changes balance of tree)

### Tree Traversal
``` Text
       B       
      / \      
     A   C     
```
- Inorder:    Left, Root, Right (A -> B -> C)
- Preorder:   root, left, right (B -> A -> C)
- Postorder:  left, right, root (A -> C -> B) 
