class Node:
    def __init__(self,ele=0,left=None,right=None):
        self.ele=ele 
        self.left=left 
        self.right=right




class Tree:
    def __init__(self):
        self.root=None 
    def Insert(self,root,ele):
        if root==None:
            return Node(ele)
        else:
            if root.ele>ele:
                root.left=self.Insert(root.left,ele)
            else:
                root.right=self.Insert(root.right,ele)
        return root





    def detetion(self,root,ele):
        if root==None:
            print("Tree is empty")
            return None
        else:
            if root.ele==ele:
                if root.left==None and root.right==None:
                    return None
                elif root.left!=None and root.right==None:
                    temp=root.left 
                    return temp 
                elif root.left==None and root.right!=None:
                    temp=root.right
                    return temp
                temp=root.right 
                while temp.left:
                    temp=temp.left
                root.ele=temp.ele 
                root.right=self.detetion(root.right,temp.ele)
                return root 
            elif ele>root.ele:
                root.right=self.detetion(root.right,ele)
            else:
                root.left=self.detetion(root.left,ele)
        return root




    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.ele)
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.ele)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.ele)

t1=Tree()
t1.root=t1.Insert(t1.root,5)


for i in range(10):
    t1.root=t1.Insert(t1.root,i)
    
t1.root=t1.detetion(t1.root,2)
t1.inorder(t1.root)