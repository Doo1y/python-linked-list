"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here


class Node:
  # TODO: Set the `_value` `_next` node instance variables
  def __init__(self, value, next=None):
    self._value = value
    self._next = next

  @property
  def value(self):
    return self._value

  @property
  def next(self):
    return self._next

  @next.setter
  def next(self, value):
    self._next = value


# TODO: Implement a Singly Linked List class here
class LinkedList:
  # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
  def __init__(self):
    self._head = None
    self._tail = None
    self._length = 0

  # TODO: Implement the get_node method here
  def get_node(self, position):
    if position > self._length:
      return None
    idx = 0
    currNode = self._head
    while idx < self._length:
      if position == idx:
        return currNode
      idx += 1
      currNode = currNode.next

  # TODO: Implement the add_to_tail method here
  def add_to_tail(self, value):
    newNode = Node(value)

    if self._tail == None:
      self._head = self._tail = newNode
    else:
      currTail = self._tail
      currTail.next = newNode
      self._tail = newNode
    self._length += 1
    return self

  # TODO: Implement the add_to_head method here

  def add_to_head(self, value):
    newNode = Node(value)

    if not self._head:
      self._head = newNode
    else:
      currNode = self._head
      self._head = newNode
      newNode.next = currNode
    self._length += 1
    return self

  # TODO: Implement the remove_head method here
  def remove_head(self):
    currNode = self._head
    if self._head:
      self._head = currNode.next
      self._length -= 1
      if self._length == 0:
        self._tail = self._head
    return currNode

  # TODO: Implement the remove_tail method here

  def remove_tail(self):
    if self._head == None or self._length == 1:
      self._head = self._tail = None
    else:
      currNode = self._head
      tail = self._tail
      for i in range(self._length - 1):
        currNode = currNode.next
      currNode.next = None
      self._tail = currNode
    if self._length != 0:
      self._length -= 1
    return self

  # TODO: Implement the __len__ method here
  def __len__(self):
    return self._length

# Phase 2

  # TODO: Implement the contains_value method here
  def contains_value(self, target):
    if self._head == None:
      return False
    currNode = self._head
    for i in range(self._length):
      if currNode.value == target:
        return True
      currNode = currNode.next
    return False

  # TODO: Implement the insert_value method here

  def insert_value(self, position, value):
    if position not in range(self._length):
      return False
    elif position == 0:
      self.add_to_head(value)
    elif position == self._length:
      self.add_to_tail(value)
    else:
      newNode = Node(value)
      prevNode = self.get_node(position)
      node_to_move = prevNode.next
      newNode.next = node_to_move
      prevNode.next = newNode
      return self

  # TODO: Implement the update_value method here
  def update_value(self, position, value):
    nodeToUpdate = self.get_node(position)
    if nodeToUpdate:
      nodeToUpdate._value = value
      return True
    return False

  # TODO: Implement the remove_node method here

  def remove_node(self, position):
    if position not in range(self._length):
      return False
    elif position == 0:
      self.remove_head()
      return True
    elif position == self._length:
      self.remove_tail()
      return True
    else:
      current_node = self._head
      previous_node = None
      counter = 0
      while counter < position:
        previous_node = current_node
        current_node = current_node.next
        counter += 1
      previous_node.next = current_node.next
      self._length -= 1
      return current_node

  # TODO: Implement the __str__ method here
  def __str__(self):
    if not self._head:
      return 'Empty List'
    node_list = []
    counter = 0
    currentNode = self._head
    while counter < self._length:
      node_list.append(currentNode._value)
      currentNode = currentNode.next
      counter += 1
    return (', ').join(node_list)

# Phase 1 Manual Testing:

# 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print(node._value)                              # hello
linked_list = LinkedList()
print(linked_list)                              # <__main__.LinkedList object at ...>

# 2. Test getting a node by its position
print(linked_list.get_node(0))                # None

# 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0).value)         # `new tail node`

# 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0).value)         # `new head node`

# i = 0
# while linked_list.get_node(i) != None:
#   print(f"current list item {i}", linked_list.get_node(i).value)
#   i += 1

# 5. Test removing the head node
linked_list.remove_head()
print(linked_list.get_node(0).value)         # `new tail node` because `new head node` has been removed
print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# 6. Test removing the tail node
print(linked_list.get_node(0).value)         # `new tail node`
linked_list.remove_tail()
print(linked_list.get_node(0))                # None

# 7. Test returning the list length
print(len(linked_list))                                 # 2

# Phase 2 Manual Testing

# 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
print(linked_list.contains_value('new head node'))      # True
print(linked_list.contains_value('App Academy node'))   # False

# 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
linked_list.insert_value(0, 'goodbye!')
print(linked_list.get_node(0)._value)                   # `goodbye!`
print(linked_list.get_node(1)._value)                   # `hello!`
print(linked_list.get_node(2).value)

# 3. Test updating a list node's value at a specific position
linked_list.update_value(0, 'goodbye!')
print(linked_list.get_node(0)._value)                   # `goodbye!`

# 4. Test removing a node value from the list at a specific position
print(linked_list.get_node(1)._value)                   # `new head node`
linked_list.remove_node(1)
print(linked_list.get_node(1))                          # None

# 5. Format the list as a string whenever `print()` is invoked
new_linked_list = LinkedList()
print(new_linked_list)                  # Empty List
new_linked_list.add_to_tail('puppies')
print(new_linked_list)                  # puppies
new_linked_list.add_to_tail('kittens')
print(new_linked_list)                  # puppies, kittens
new_linked_list.add_to_tail('cats')
new_linked_list.add_to_tail('dogs')
new_linked_list.add_to_head('penguins')
print(new_linked_list)                  # penguins, puppies, kittens, cats, dogs
