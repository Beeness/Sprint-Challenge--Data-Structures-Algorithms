class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #RECURSIVE VERSION****
    #call the cb on the current BEST node
    #left side
    cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
    #right side
    if self.right:
      self.right.depth_first_for_each(cb)
    
    """
   #***ITERATIVE VERSION****
    stack = []
    #append the root node of our BST
    stack.append(.self)
    #iterate through the elements in the stackk
    while len(stack):
      #pop off the top-most stack element
      current_node = stack.pop()
      #check to see if this node has a right child
      if current_node.right:
        stack.append(current_node.right)
      #check to see if this node has a left child
      if current_node.left:
        stack.append(current_node.left)
      #don't forget to call the callback
      cb(current_node.value)
    """

  

  def breadth_first_for_each(self, cb):
    #use an array
    queue = []

    #push our node onto it
    queue.append(self)

    #loop through the queue until it's empty
    while len(queue) > 0:
      node = queue.pop(0)

      # add the node's children to the queue if they exist
      if node.left:
        queue.append(node.left)

      if node.right:
        queue.append(node.right)

      # use the callback
      cb(node.value)
  

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
