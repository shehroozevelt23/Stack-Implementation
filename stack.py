class Single:
    """
    Fields: _value stores any value
            _next stores the next node or None, if none
    """

    ## Single(value) produces a newly constructed singly-linked node
    ##     storing value.
    ## __init__: Any -> Single
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

    ## repr(self) produces a string with the information in self.
    ## __repr__: Single -> Str
    def __repr__(self):
        if self._value == None:
            return "Empty node"
        else:
            return str("Node containing " + self._value)

    ## self.access() produces the value stored in self.
    ## access: Single -> Any
    def access(self):
        return self._value

    ## self.next() produces the node to which self is linked
    ##    or None if none exists.
    ## next: Single -> (anyof Single None)
    def next(self):
        return self._next

    ## self.store(value) stores value in self.
    ## Effects: Mutates self by storing value in self.
    ## store: Single Any -> None
    def store(self, value):
        self._value = value

    ## self.link(node) links node using the next pointer.
    ## Effects: Mutates self by linking node using the next pointer.    
    ## link: Single (anyof Single None) -> none
    def link(self, node):
        self._next = node
        


class Stack:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def push(self, data):
        Node = Single(data)
        Node._next = self.head
        self.head = Node
        
    def top(self):
        if self.is_empty() == False:
            return self.head._value
        else:
            return None
        
    def pop(self):
        if self.is_empty() == True:
            return None
        else:
            ret = self.head._value
            self.head = self.head._next
            return ret
        
        
        

