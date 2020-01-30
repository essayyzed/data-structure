class HashMap:
    
    def __init__(self):
        
        self.size = 10
        self.map = [None] * self.size
###############################################

def _get_hash(self , key):
    
    if type(key) == str:
        
        return ASCII(key) % self.size
    if type(key) == tuple:
        return sum(key) % self.size
    
    if type(key) == int:
        return key % self.size

HashMap._get_hash = _get_hash
##############################################

def ASCII(s):
    x = 0
    for i in range(len(s)):
        x += ord(s[i])*2**(8 * (len(s) - i - 1))
    return x

################################################

def get(self, key):
    
    key_hash = self._get_hash(key)
    
    if self.map[key_hash] is not None:
        
        for pair in self.map[key_hash]:
            
            if pair[0] == key:
                return pair[1]
            
    raise KeyError(str(key))
    
HashMap.get = get
################################################

def __str__(self):
    
    ret = " "
    
    for i , item in enumerate(self.map):
        
        if item is not None:
            
            ret += str(i) + " : " + str(item) + '\n'
            
    return ret

HashMap.__str__ = __str__



def add(self, key, value):
    
    key_hash = self._get_hash(key)
    key_value = [key , value]
    
    if self.map[key_hash] is None:
        
        self.map[key_hash] = [key_value]
        return True
    
    else:
        for pair in self.map[key_hash]:
            
            if pair[0] == key:
                
                print('updating : ', key)
                pair[1] = value
                return True
            
    self.map[key_hash].append(key_value)
HashMap.add = add
    

def delete(self, key):
    key_hash = self._get_hash(key)
    
    if self.map[key_hash] is None:
        raise KeyError(str(key))
        
    for i in range(0, len(self.map[key_hash])):
        
        if self.map[key_hash][i][0] == key:
            self.map[key_hash].pop(i)
            return True
HashMap.delete = delete



if __name__ == '__main__': 
    h = HashMap() 

    h.add(17, "seventeen")
    h.add(26, "twenty six")
    h.add(35, "thirty five")
    h.add(25, "twenty five")
    h.add(26, "twenty six updated")
    h.add(887, "large number")

    print(h)