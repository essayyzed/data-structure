class Person:
    
    def __init__(self , name , age , queue_number):
        self.name = name
        self.age = age
        self.queue_number = queue_number


def build_heap(lst):
    n = len(lst)
    for i in reversed(range(n//2)):
        heapify(lst,n,i)

def heapify(lst,n,root):
    
    smallest = root
    left = 2*root + 1
    right = 2*root + 2
    
    if left < n and lst[left].get_priority() < lst[smallest].get_priority():
        smallest = left
    
    if right < n and lst[right].get_priority() < lst[smallest].get_priority():
        smallest = right
    
    if root != smallest:
        lst[root],lst[smallest] = lst[smallest],lst[root]
        heapify(lst,n,smallest)

def heap_sort(lst):
    
    n = len(lst)
    
    build_heap(lst)
    for i in reversed(range(n)):
        lst[i],lst[0] = lst[0],lst[i]
        heapify(lst,i,0)

###################################################################################################################################################


def get_priority(self):
    
    priority = 100 - self.queue_number
    
    if self.age >= 40:
        
        priority += 100
        
        return priority
    else:
        return priority
    
Person.get_priority = get_priority


def __str__(self):

    ret_str = self.name + ' ' + str(get_priority(self))

    return ret_str
Person.__str__ = __str__

if __name__ == '__main__': 
    p = Person('A', 24, 1) 
    print(p) # should output: A 99

    p = Person('A', 40, 1) 
    print(p) # should output: A 199
    
    people = [ 
        Person('A', 24, 1), 
        Person('B', 32, 2), 
        Person('C', 45, 3), 
        Person('D', 22, 4), 
        Person('E', 21, 5), 
        Person('F', 32, 6), 
        Person('G', 39, 7), 
        Person('H', 44, 8), 
        Person('I', 22, 9), 
        Person('J', 29, 10), 
        Person('K', 32, 11), 
        Person('L', 31, 12) 
    ]
    
    print([str(p)  for p in people])
    heap_sort(people) 
    print([str(p)  for p in people])
    # sould output: 
    # ['C 197', 'H 192', 'A 99', 'B 98', 'D 96', 'E 95', 'F 94', 'G 93', 'I 91', 'J 90', 'K 89', 'L 88']