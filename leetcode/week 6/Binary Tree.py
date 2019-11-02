
  

class ListNode: 
  
        # Constructor to create a new node 
        def __init__(self, data): 
            self.data = data 
            self.next = None
  

class BinaryTreeNode: 
  
     
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
 
class Conversion: 
  
    
    def __init__(self, data = None): 
        self.head = None
        self.root = None
  
    def push(self, new_data): 
  
       
        new_node = ListNode(new_data) 
  
       
        new_node.next = self.head 
  
        
        self.head = new_node 
  
    def convertList2Binary(self): 
  
        
        q = [] 
  
        
        if self.head is None: 
            self.root = None
            return 
  
       
        self.root = BinaryTreeNode(self.head.data) 
        q.append(self.root) 
  
       
        self.head = self.head.next
  
        
        while(self.head): 
  
           
            parent = q.pop(0) # Front of queue 
  
          
            leftChild= None
            rightChild = None
  
            leftChild = BinaryTreeNode(self.head.data) 
            q.append(leftChild) 
            self.head = self.head.next
            if(self.head): 
                rightChild = BinaryTreeNode(self.head.data) 
                q.append(rightChild) 
                self.head = self.head.next
  
            
            parent.left = leftChild 
            parent.right = rightChild 
  
    def inorderTraversal(self, root): 
        if(root): 
            self.inorderTraversal(root.left) 
            print root.data, 
            self.inorderTraversal(root.right) 
  

conv = Conversion() 
conv.push(36) 
conv.push(30) 
conv.push(25) 
conv.push(15) 
conv.push(12) 
conv.push(10) 
  
conv.convertList2Binary() 
  
print "Inorder Traversal of the contructed Binary Tree is:"
conv.inorderTraversal(conv.root) 
  
