#!/usr/bin/env python
# coding: utf-8

# In[1]:


def heapify(lst, n, root):
    
    largest = root
    l = 2*root + 1
    r = 2*root + 1
    
    if l < n and lst[l] > lst[largest]:
        largest = l
        
    if r < n and lst[r] > lst[largest]:
        largest = r
        
    if largest != root:
        lst[root], lst[largest] = lst[largest] , lst[root]
        
        heapify(lst, n, largest) 


# In[2]:


def build_heap(lst):
    
    n = len(lst)
    
    for i in reversed(range(n // 2)):
        heapify(lst, n, i)


# In[3]:


heap = [100, 5, 3, 2, 8, 15, 6, 102]


# In[4]:


print(heap)
build_heap(heap)
print(heap)


# In[5]:


def heap_sort(lst):
    
    n = len(lst)
    
    build_heap(lst)
    
    for i in reversed(range(n)):
        lst[i], lst[0] = lst[0], lst[i]
        
        heapify(lst, i, 0)


# In[7]:


heap = [100, 5, 3, 2, 8, 15, 6, 102]
print(heap)
heap_sort(heap)
print(heap)

