import warnings

from extra.lists.queue import Queue




class Deque(Queue):
    """Basic object for the Deque data structure"""
    def __name__(self):
        return "extra.Deque()"
    

    ############################## PRINT ##############################
    def __repr__(self):
        """Represents the deque as a string."""
        return super()._print_queue('⟷')

    
    ############################## GET ################################
    def get_last(self):
        """Returns the Qeueu tail (last element to be enqueued) """
        if self.is_empty():
            raise IndexError(\
                f"Can't retrieve from an empty {self.__name__()}!!")
        return self.container.tail.get_data()


    ############################# APPEND ##############################
    def append_first(self, item):
        """Insert value into the front of the Deque"""
        super()._validate_item(item)
        if self.is_full():
            self.container.remove_end()
        self.container.add_front(item)


    def append_last(self, item):
        """Insert value into the end of the Deque"""
        super().enqueue(item)


    ############################## POP ###############################
    def pop_first(self):
        """Removes value from the Deque (first-inserted item)"""
        return super().dequeue()


    def pop_last(self):
        """Removes value from the Deque (most recent)"""
        if self.is_empty():
            warnings.warn(f"Dequeuing from an empty {self.__name__()}!!")
            return None
        else:
            return self.container.remove_end().get_data()




if __name__ == "__main__":
    q = Deque(max_capacity=3)
    q.append_left(0)    #0
    q.append_right(1)   #0 1
    q.append_right(8)   #0 1 8
    q.append_left(9)    #9 0 1
    print(q)
    