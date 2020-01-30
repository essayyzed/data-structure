class Node:
    def __init__(self, data = None):
        self.val = data
        self.next = None



class Ring:
    def __init__(self):
        self.head = None





def __str__(self):

    ret_str = '['
    temp = self.head
    while temp is not None:
        ret_str += str(temp.val) + ', '
        temp = temp.next
        
        if temp == self.head:
            break
            
    ret_str = ret_str.rstrip(', ')
    ret_str += ']'
        
    return ret_str   
Ring.__str__ = __str__





def _get_last(self):
    
    if self.head is None:
        return None
    
    temp = self.head.next
    while temp.next != self.head:
        temp = temp.next
        
    return temp
Ring._get_last = _get_last





def insert(self, index, val):


    new_node = Node(val)
    last = self._get_last()

    if index == 0 or self.head is None:

        new_node.next = self.head
        self.head = new_node

        if last is None:
            self.head.next = self.head
        else:
            last.next = new_node

        return

    temp = self.head
    counter = 0

    while temp is not None and counter < index:
        prev = temp
        temp = temp.next
        counter += 1

    prev.next = new_node
    new_node.next = temp
Ring.insert = insert





def remove(self, val):
    if self.head is None:
        return
    
    temp = self.head
    last =self._get_last()
    
    if temp.val == val:
        if last == self.head:
            self.head = None
            
        else:
            self.head = temp.next
            last.next = self.head
        return
    prev = temp
    temp = temp.next
    
    while temp != self.head:
        if temp.val == val:
            break
            
        prev = temp
        temp = temp.next
    if temp == self.head:
        return
    prev.next = temp.next
Ring.remove = remove  





def remove_at(self, index):
    
    temp = self.head
    if self.len() == 0:
        return
    
    if temp.val == self.get(index):
        if temp.next == self.head:
            self.head = None
            return
        
        else:
            last = self._get_last()
            last.next = self.head.next
            self.head = last.next
            return
    
    while temp.next.val != self.get(index):
        temp = temp.next
        
    temp.next = temp.next.next
    return     
Ring.remove_at = remove_at





def push(self, val):
    
    new_node = Node(val)
    
    if self.head is None:
        
        print("1st Case")
        self.head = new_node
        new_node.next = self.head
        return

    temp = self.head
    counter = 1
    while temp.next != self.head:
        
        temp = temp.next
        counter += 1
    self.insert(counter, val)  
Ring.push = push




def pop(self):

    if self.head is None:
        raise Exception("Cannot Pop. No Value")
        
    if self.head.next == self.head:
        val = self.head.val
        self.head = None
        return val
    
    temp = self.head
    while temp.next != self.head:
        prev = temp
        temp = temp.next
        
    val = temp.val
    prev.next = self.head
    return val
Ring.pop = pop




def len(self):
    
    if self.head is None:
        return 0
        
    if self.head.next == self.head:
        return 1
    
    counter = 1
    temp = self.head.next
    
    
    while temp != self.head:
        temp = temp.next
        counter += 1
        
    
    return counter
Ring.len = len




def get(self , index):
    
    if self.head is None:
        raise IndexError("IndexError: Index out of bound")
    
    if index == 0:
        return self.head.val
    
    temp = self.head
    counter = 0
    
    while counter < index:
        prev = temp
        temp = temp.next
        counter += 1
            
    if counter == index:
        return temp.val

    
Ring.get = get


if __name__ == '__main__': 
    r = Ring()
    r.insert(1, 1)
    r.insert(0, 1)
    r.insert(0, 2)
    r.insert(1, 3)
    r.insert(7, 5)  # different behavrior since it's a ring! 
    print(r)
