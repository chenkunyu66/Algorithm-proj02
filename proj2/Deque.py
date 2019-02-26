#project 02
#cse 331
#chen,kunyu
#A54470631

#make a Node class to create a double linked list 
class Node():
    def __init__(self, data, prev, nxt):
        self._data = data
        self._next= nxt
        self._previous = prev

    def set_next(self, nxt):
        self._next = nxt

    def get_next(self):
        return self._next

    def set_prev(self, prev):
        self._previous = prev
        
    def get_prev(self):
        return self._previous

    def set_data(self, dat):
        self._data = dat

    def get_data(self):
        return self._data
        
class Deque:
    """
    A double-ended queue
    """

    def __init__(self):
        """
        Initializes an empty Deque
        """
        # make the head and tail = None
        self._head = None
        self._tail = None
        self._size = 0
    

    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The logical size of the Deque
        """
        #return the size of deque
        return self._size

    def peek_front(self):
        """
        Looks at, but does not remove, the first element
        :return: The first element
        """
        #empty check 
        if self._size <= 0:
            raise IndexError
        #return head data
        return self._head.get_data()

    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        """
        #empty check 
        if self._size <= 0:
            raise IndexError

        #return tail data 
        return self._tail.get_data()

    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """
        #new node 
        New_node = Node(e, None, None)
        #if size is 0
        if self._size==0:
            self._head = self._tail = New_node
        else:
            
            New_node.set_next(self._head)
            self._head.set_prev(New_node)
            #head point to new node
            self._head = New_node

        self._size+=1
        
    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """
        New_node = Node(e, None, None)
        if self._size==0:
            self._head = self._tail = New_node
        else:
            New_node.set_prev(self._tail)
            self._tail.set_next(New_node)
            self._tail = New_node

        self._size+=1

    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        """
        #empty check
        if self._size == 0:
            raise IndexError

        tmp = self._head.get_data()

        self._head = self._head.get_next()
        
        if self._head is None:
            self._tail=None

        self._size-=1

        return tmp

    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        """
        if self._size == 0:
            raise IndexError

        tmp= self._tail.get_data()
        self._tail= self._tail.get_prev()

        if self._tail is None:
            self._head=None

        self._size-=1

        return tmp

    def clear(self):
        """
        Removes all elements from the Deque
        :return:
        """
        while self._size > 0:
            self.pop_back()

    def retain_if(self, condition):
        """
        Removes items from the Deque so that only items satisfying the given condition remain
        :param condition: A boolean function that tests elements
        """
        element = self._head  
        while element:
            if not condition(element.get_data()):# if no conditon 
                if element.get_prev() is None:
                    element = element.get_next()
                    self.pop_front()
                elif element.get_next() is None:
                    self.pop_back()
                else:
                    element.get_prev().set_next(element.get_next())
                    element.get_next().set_prev(element.get_prev())
                    self._size-=1#size-1 chang index
                    element = element.get_next()
            else:
                element=element.get_next()
                    
        
    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        """
        new_node = self._head
        for i in range(self._size):
            yield new_node.get_data()
            new_node = new_node.get_next()


    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0

    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))


