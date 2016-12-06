def check_binary_search_tree_(root):
    if(not(root.left is None)):
        if(root.data < root.left.data):
            return False;
        else:
            return check_binary_search_tree_(root.left)

    if(not(root.right is None)):
        if(root.data > root.right.data):
            return False
        else:
            return check_binary_search_tree_(root.right)

    return True
